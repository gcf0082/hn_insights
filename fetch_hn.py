import requests
import time
import re
import os
import subprocess
from datetime import datetime, timezone, timedelta

try:
    import yaml
except ImportError:
    print("PyYAML not found. Installing...")
    os.system("pip install pyyaml -q")
    import yaml

HN_API_BASE = "https://hacker-news.firebaseio.com/v0"
MAX_RETRIES = 3
RETRY_DELAY = 2
CONFIG_PATH = "config.yaml"
BEIJING_TZ = timezone(timedelta(hours=8))


def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_min_score(score, config):
    if not config:
        return True

    min_score = config.get("min_score", 0)
    if score is None:
        return True

    return score >= min_score


def check_min_descendants(descendants, config):
    if not config:
        return True

    min_descendants = config.get("min_descendants", 0)
    if descendants is None:
        return True

    return descendants >= min_descendants


def match_title_rules(title, config):
    if not config:
        return True

    title_rules = config.get("title_rules", [])
    if not title_rules:
        return True

    for rule in title_rules:
        if not rule.get("enabled", True):
            continue

        keywords = rule.get("keywords", [])
        if not keywords:
            continue

        ignore_case = rule.get("ignore_case", True)
        match_type = rule.get("match_type", "contains")

        search_title = title.lower() if ignore_case else title

        for keyword in keywords:
            search_keyword = keyword.lower() if ignore_case else keyword

            if match_type == "word":
                pattern = r"\b" + re.escape(search_keyword) + r"\b"
                if re.search(pattern, search_title):
                    return True
            else:
                if search_keyword in search_title:
                    return True

    return False


def fetch_with_retry(url, max_retries=MAX_RETRIES):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException,
        ) as e:
            if attempt < max_retries - 1:
                print(
                    f"\n  Retry {attempt + 1}/{max_retries} after error: {type(e).__name__}"
                )
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise


def fetch_story_ids():
    url = f"{HN_API_BASE}/topstories.json"
    return fetch_with_retry(url)


def fetch_story_detail(story_id):
    url = f"{HN_API_BASE}/item/{story_id}.json"
    return fetch_with_retry(url)


def insight_exists(story_id, suffix):
    if not os.path.exists("insights"):
        return None

    pattern = f"_{story_id}_{suffix}"
    for filename in os.listdir("insights"):
        if pattern in filename and filename.endswith(".md"):
            return filename
    return None


def generate_insight(story_id, url, date_prefix, suffix="", chinese_title=None):
    os.makedirs("insights", exist_ok=True)

    if suffix:
        insight_file = f"{date_prefix}_{story_id}_{suffix}.md"
    else:
        insight_file = f"{date_prefix}_{story_id}.md"

    print(f"\n  Generating insight for story {story_id}...")
    print(f"  URL: {url}")
    print(f"  Output: insights/{insight_file}")

    cmd = [
        "opencode",
        "run",
        f"帮我总结洞察{url}。要求：报告必须是中文的，报告顶部包含洞察链接和基本信息，洞察结果保存在当前目录的 insights 目录的{insight_file}",
        "--model",
        "opencode/minimax-m2.5-free",
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

    if chinese_title:
        chinese_title = sanitize_filename(chinese_title)
        base_name = (
            f"{date_prefix}_{story_id}_{suffix}"
            if suffix
            else f"{date_prefix}_{story_id}"
        )
        new_insight_file = f"{base_name}_{chinese_title}.md"
        old_path = f"insights/{insight_file}"
        new_path = f"insights/{new_insight_file}"
        try:
            os.rename(old_path, new_path)
            print(f"  Renamed to: {new_insight_file}")
            insight_file = new_insight_file
        except Exception as e:
            print(f"  Warning: Failed to rename file: {type(e).__name__}: {e}")

    return insight_file


def convert_title_to_chinese(title):
    print(f"  Converting title to Chinese: {title}")
    cmd = [
        "opencode",
        "run",
        f'帮我把如下标题转换成中文标题(只输出结果不解释)，待翻译标题："{title}"',
        "--model",
        "opencode/minimax-m2.5-free",
    ]

    print(f"  Running: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, timeout=60, capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            chinese_title = result.stdout.strip()
            print(f"  Chinese title: {chinese_title}")
            return chinese_title
        else:
            print(f"  Warning: Title conversion failed with code {result.returncode}")
            return None
    except subprocess.TimeoutExpired:
        print(f"  Warning: Title conversion timeout")
        return None
    except Exception as e:
        print(f"  Warning: {type(e).__name__}: {e}")
        return None


def sanitize_filename(filename):
    filename = filename.replace("/", " ").replace("\\", " ")
    filename = filename.replace(":", " ").replace("*", " ").replace("?", " ")
    filename = (
        filename.replace('"', "").replace("<", " ").replace(">", " ").replace("|", " ")
    )
    filename = filename.strip()
    if len(filename) > 100:
        filename = filename[:100]
    return filename


def main():
    print("Loading config...")
    config = load_config()

    if config:
        min_score = config.get("min_score", 0)
        min_descendants = config.get("min_descendants", 0)
        print(f"Min score: {min_score}")
        print(f"Min descendants: {min_descendants}")

        title_rules = config.get("title_rules", [])
        print(f"Title rules: {len(title_rules)} rules")
        for i, rule in enumerate(title_rules, 1):
            match_type = rule.get("match_type", "contains")
            keywords = rule.get("keywords", [])
            print(f"  Rule {i}: {match_type} - {keywords}")
    else:
        print("No config file found, fetching all stories")

    print("\nFetching top story IDs...")
    story_ids = fetch_story_ids() or []
    # story_ids = story_ids[:100]
    print(f"Found {len(story_ids)} stories\n")

    processed_count = 0
    skipped_count = 0
    filtered_score_count = 0
    filtered_descendants_count = 0
    filtered_title_count = 0
    error_count = 0
    date_prefix = datetime.now(BEIJING_TZ).strftime("%Y%m%d_%H%M%S")
    for i, story_id in enumerate(story_ids, 1):
        print(f"Fetching story {i}/{len(story_ids)} (ID: {story_id})...", end="\r")
        try:
            story = fetch_story_detail(story_id)

            if story:
                title = story.get("title", "")
                score = story.get("score")
                descendants = story.get("descendants")
                original_url = story.get("url")

                if not check_min_score(score, config):
                    filtered_score_count += 1
                    continue

                if not check_min_descendants(descendants, config):
                    filtered_descendants_count += 1
                    continue

                if not match_title_rules(title, config):
                    filtered_title_count += 1
                    continue

                hn_url = f"https://news.ycombinator.com/item?id={story_id}"

                # 检查是否已存在洞察文件
                existing_hn = insight_exists(story_id, "hn")
                existing_article = (
                    insight_exists(story_id, "article") if original_url else None
                )

                # hn 必须存在，如果有 original_url 则 article 也必须存在
                need_hn = not existing_hn
                need_article = original_url and not existing_article

                if not need_hn and not need_article:
                    print(f"\n  Story {story_id} already has all insights, skipping")
                    skipped_count += 1
                    continue

                print(f"\n  Processing story {story_id}: {title}")

                # 在生成洞察前转换标题
                chinese_title = convert_title_to_chinese(title)

                # 1. 生成 HN 洞察
                if need_hn:
                    print(f"  Generating HN insight...")
                    hn_insight_file = generate_insight(
                        story_id,
                        hn_url,
                        date_prefix,
                        suffix="hn",
                        chinese_title=chinese_title,
                    )

                    if not hn_insight_file or not os.path.exists(
                        f"insights/{hn_insight_file}"
                    ):
                        print(f"  Error: HN insight not generated for story {story_id}")
                        error_count += 1
                        continue

                # 2. 生成 article 洞察
                if need_article:
                    print(f"  Generating article insight...")
                    article_insight_file = generate_insight(
                        story_id,
                        original_url,
                        date_prefix,
                        suffix="article",
                        chinese_title=chinese_title,
                    )

                    if not article_insight_file or not os.path.exists(
                        f"insights/{article_insight_file}"
                    ):
                        print(
                            f"  Error: article insight not generated for story {story_id}"
                        )
                        error_count += 1
                        continue

                processed_count += 1
        except Exception as e:
            error_count += 1
            print(f"\n  Error fetching story {story_id}: {type(e).__name__}")
            continue

    print(f"\n\nDone!")
    print(f"  Processed: {processed_count}")
    print(f"  Skipped (already exists): {skipped_count}")
    print(f"  Filtered (low score): {filtered_score_count}")
    print(f"  Filtered (low comments): {filtered_descendants_count}")
    print(f"  Filtered (title not matched): {filtered_title_count}")
    print(f"  Errors: {error_count}")


if __name__ == "__main__":
    main()
