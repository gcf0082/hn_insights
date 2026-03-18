import sqlite3
import json
import os
from datetime import datetime

DB_PATH = "hacknews.db"
DATA_DIR = "data"

def get_today_stories():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute('''
        SELECT id, hn_url, original_url, by, title, score, time, descendants, type, fetched_at
        FROM stories
        WHERE DATE(fetched_at) = DATE(?)
        ORDER BY score DESC
    ''', (today,))
    
    rows = cursor.fetchall()
    conn.close()
    
    stories = []
    for row in rows:
        stories.append({
            'id': row['id'],
            'hn_url': row['hn_url'],
            'original_url': row['original_url'],
            'by': row['by'],
            'title': row['title'],
            'score': row['score'],
            'time': row['time'],
            'descendants': row['descendants'],
            'type': row['type'],
            'fetched_at': row['fetched_at']
        })
    
    return stories

def main():
    stories = get_today_stories()
    
    if not stories:
        print("No stories found for today")
        return
    
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    today = datetime.now().strftime('%Y%m%d')
    output_file = os.path.join(DATA_DIR, f"{today}.json")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(stories, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(stories)} stories to {output_file}")

if __name__ == "__main__":
    main()