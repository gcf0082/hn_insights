import sqlite3
import requests
import time
import re
import os
import subprocess
from datetime import datetime

try:
    import yaml
except ImportError:
    print("PyYAML not found. Installing...")
    os.system('pip install pyyaml -q')
    import yaml

DB_PATH = "hacknews.db"
HN_API_BASE = "https://hacker-news.firebaseio.com/v0"
MAX_RETRIES = 3
RETRY_DELAY = 2
CONFIG_PATH = "config.yaml"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def check_min_score(score, config):
    if not config:
        return True
    
    min_score = config.get('min_score', 0)
    if score is None:
        return True
    
    return score >= min_score

def check_min_descendants(descendants, config):
    if not config:
        return True
    
    min_descendants = config.get('min_descendants', 0)
    if descendants is None:
        return True
    
    return descendants >= min_descendants

def match_title_rules(title, config):
    if not config:
        return True
    
    title_rules = config.get('title_rules', [])
    if not title_rules:
        return True
    
    for rule in title_rules:
        if not rule.get('enabled', True):
            continue
        
        keywords = rule.get('keywords', [])
        if not keywords:
            continue
        
        ignore_case = rule.get('ignore_case', True)
        match_type = rule.get('match_type', 'contains')
        
        search_title = title.lower() if ignore_case else title
        
        for keyword in keywords:
            search_keyword = keyword.lower() if ignore_case else keyword
            
            if match_type == 'word':
                pattern = r'\b' + re.escape(search_keyword) + r'\b'
                if re.search(pattern, search_title):
                    return True
            else:
                if search_keyword in search_title:
                    return True
    
    return False

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY,
            hn_url TEXT UNIQUE NOT NULL,
            original_url TEXT,
            by TEXT,
            title TEXT,
            score INTEGER,
            time INTEGER,
            descendants INTEGER,
            type TEXT,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_hn_url ON stories(hn_url)')
    conn.commit()
    return conn

def fetch_with_retry(url, max_retries=MAX_RETRIES):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.ConnectionError, 
                requests.exceptions.Timeout,
                requests.exceptions.RequestException) as e:
            if attempt < max_retries - 1:
                print(f"\n  Retry {attempt + 1}/{max_retries} after error: {type(e).__name__}")
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise

def fetch_story_ids():
    url = f"{HN_API_BASE}/topstories.json"
    return fetch_with_retry(url)

def fetch_story_detail(story_id):
    url = f"{HN_API_BASE}/item/{story_id}.json"
    return fetch_with_retry(url)

def insert_story(conn, story):
    cursor = conn.cursor()
    story_id = story.get('id')
    hn_url = f"https://news.ycombinator.com/item?id={story_id}"
    original_url = story.get('url')
    by = story.get('by')
    title = story.get('title')
    score = story.get('score')
    time_stamp = story.get('time')
    descendants = story.get('descendants')
    story_type = story.get('type')
    
    try:
        cursor.execute('''
            INSERT INTO stories (id, hn_url, original_url, by, title, score, time, descendants, type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (story_id, hn_url, original_url, by, title, score, time_stamp, descendants, story_type))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def story_exists(conn, story_id):
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM stories WHERE id = ?', (story_id,))
    return cursor.fetchone() is not None

def generate_insight(story_id, original_url):
    os.makedirs("insights", exist_ok=True)
    
    date_prefix = datetime.now().strftime("%Y%m%d_%H%M%S")
    insight_file = f"insights/{date_prefix}_{story_id}.md"
    
    print(f"\n  Generating insight for story {story_id}...")
    print(f"  URL: {original_url}")
    print(f"  Output: {insight_file}")
    
    cmd = [
        "opencode", "run",
        f"帮我总结洞察{original_url}，洞察结果保存在当前目录的insights目录的{date_prefix}_{story_id}.md",
        "--model", "opencode/minimax-m2.5-free"
    ]
    
    print(f"  Running: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, timeout=300)
        print(f"  Command finished with return code: {result.returncode}")
        if result.returncode != 0:
            print(f"  Error: opencode command failed with code {result.returncode}")
            return None
    except subprocess.TimeoutExpired:
        print(f"  Error: opencode command timeout after 5 minutes")
        return None
    except Exception as e:
        print(f"  Error: {type(e).__name__}: {e}")
        return None
    
    return insight_file

def main():
    print("Loading config...")
    config = load_config()
    
    if config:
        min_score = config.get('min_score', 0)
        min_descendants = config.get('min_descendants', 0)
        print(f"Min score: {min_score}")
        print(f"Min descendants: {min_descendants}")
        
        title_rules = config.get('title_rules', [])
        print(f"Title rules: {len(title_rules)} rules")
        for i, rule in enumerate(title_rules, 1):
            match_type = rule.get('match_type', 'contains')
            keywords = rule.get('keywords', [])
            print(f"  Rule {i}: {match_type} - {keywords}")
    else:
        print("No config file found, fetching all stories")
    
    print("\nConnecting to database...")
    conn = create_database()
    
    print("Fetching top story IDs...")
    story_ids = fetch_story_ids()
    story_ids = story_ids[:100]
    print(f"Found {len(story_ids)} stories\n")
    
    new_count = 0
    existing_count = 0
    filtered_score_count = 0
    filtered_descendants_count = 0
    filtered_title_count = 0
    error_count = 0
    
    for i, story_id in enumerate(story_ids, 1):
        print(f"Fetching story {i}/{len(story_ids)} (ID: {story_id})...", end='\r')
        try:
            story = fetch_story_detail(story_id)
            
            if story:
                title = story.get('title', '')
                score = story.get('score')
                descendants = story.get('descendants')
                original_url = story.get('url')
                
                if not check_min_score(score, config):
                    filtered_score_count += 1
                    continue
                
                if not check_min_descendants(descendants, config):
                    filtered_descendants_count += 1
                    continue
                
                if not match_title_rules(title, config):
                    filtered_title_count += 1
                    continue
                
                if story_exists(conn, story_id):
                    print(f"\n  Story {story_id} already exists in database")
                    existing_count += 1
                    continue
                
                print(f"\n  Processing new story {story_id}: {title}")
                if original_url:
                    print(f"  Has original_url, generating insight...")
                    insight_file = generate_insight(story_id, original_url)
                    
                    print(f"  Insight file returned: {insight_file}")
                    if insight_file:
                        print(f"  File exists check: {os.path.exists(insight_file)}")
                    
                    if not insight_file or not os.path.exists(insight_file):
                        print(f"  Error: insight not generated for story {story_id}")
                        error_count += 1
                        continue
                else:
                    print(f"  No original_url, skipping insight generation")
                
                print(f"  Inserting story {story_id} into database...")
                if insert_story(conn, story):
                    new_count += 1
                    print(f"  Story {story_id} inserted successfully")
        except Exception as e:
            error_count += 1
            print(f"\n  Error fetching story {story_id}: {type(e).__name__}")
            continue
    
    print(f"\n\nDone!")
    print(f"  New stories: {new_count}")
    print(f"  Already existed: {existing_count}")
    print(f"  Filtered (low score): {filtered_score_count}")
    print(f"  Filtered (low comments): {filtered_descendants_count}")
    print(f"  Filtered (title not matched): {filtered_title_count}")
    print(f"  Errors: {error_count}")
    
    conn.close()

if __name__ == "__main__":
    main()