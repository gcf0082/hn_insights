# AGENTS.md

Coding agent guidelines for the hn_insights repository.

## Project Overview

This project fetches Hacker News stories and generates AI-powered insights:
- **Python backend**: `fetch_hn.py` (fetches stories, generates insights via opencode CLI)
- **Python export**: `export_today.py` (exports stories to JSON)
- **Frontend**: `docs/` directory (HTML/CSS/JS for viewing insights)
- **Configuration**: `config.yaml` (filters for story selection)
- **Data**: SQLite database (`hacknews.db`) and JSON files in `data/`

## Build/Lint/Test Commands

### Setup
```bash
pip install requests pyyaml
```

### Run Commands
```bash
python fetch_hn.py          # Fetch HN stories and generate insights
python export_today.py      # Export today's stories to JSON
```

### Lint/Type Check (Recommended)
Since this project has no formal linting setup, consider installing:
```bash
pip install ruff mypy
ruff check .                # Lint Python files
mypy fetch_hn.py export_today.py  # Type check
```

### Testing
No test suite exists. To run a single test (if added later):
```bash
pytest tests/test_file.py::test_name -v
```

### GitHub Actions
The workflow `.github/workflows/fetch_hn.yml` runs every 2 hours. Manual trigger available via workflow_dispatch.

## Code Style Guidelines

### Python Style

#### Imports
- Standard library imports first, then third-party, then local
- Group imports with blank lines between sections
- Use explicit imports (avoid `from module import *`)
- Handle missing dependencies gracefully with try/except

```python
import requests
import time
import os
from datetime import datetime, timezone, timedelta

try:
    import yaml
except ImportError:
    print("PyYAML not found. Installing...")
    os.system("pip install pyyaml -q")
    import yaml
```

#### Formatting
- 4 spaces for indentation (no tabs)
- Maximum line length: ~100 characters
- Blank lines between function definitions

#### Naming Conventions
- **Functions**: `snake_case` (e.g., `fetch_story_ids`, `load_config`)
- **Variables**: `snake_case` (e.g., `story_ids`, `chinese_title`)
- **Constants**: `UPPER_SNAKE_CASE` at module level (e.g., `HN_API_BASE`, `MAX_RETRIES`)

#### Error Handling
- Use specific exception types (e.g., `requests.exceptions.ConnectionError`)
- Handle network-related exceptions with retry logic
- Print descriptive error messages with exception type

```python
except (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.RequestException,
) as e:
    if attempt < max_retries - 1:
        print(f"\n  Retry {attempt + 1}/{max_retries} after error: {type(e).__name__}")
        time.sleep(RETRY_DELAY * (attempt + 1))
    else:
        raise
```

#### String Formatting
- Use f-strings for string interpolation
- Use double quotes for strings with Chinese characters

### JavaScript Style (docs/js/app.js)
- **Variables/Functions**: `camelCase` (e.g., `fetchPosts`, `allPosts`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `REPO_OWNER`, `PAGE_SIZE`)
- 4 spaces for indentation; use `const` and `let`; async/await for async operations

### Configuration (config.yaml)
- Use 2 spaces for indentation; group related settings together

```yaml
min_score: 50
min_descendants: 20
title_rules:
  - match_type: "word"
    ignore_case: true
    keywords: ["AI", "LLM"]
```

## File Structure

```
hn_insights/
fetch_hn.py              # Main fetch script
export_today.py          # Export utility
config.yaml              # Filter configuration
hacknews.db              # SQLite database
insights/                # Generated markdown insights
data/                    # Exported JSON files
docs/
  index.html             # Frontend entry
  css/style.css          # Styles
  js/app.js              # Frontend logic
.github/
  workflows/
    fetch_hn.yml         # CI/CD workflow
```

## Key Patterns

### Retry Logic
Implement exponential backoff for network requests:
```python
def fetch_with_retry(url, max_retries=MAX_RETRIES):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except (...) as e:
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))
            else:
                raise
```

### Configuration Loading
Always check if config exists before accessing:
```python
def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
```

### File Naming Convention
Insights are named: `{YYYYMMDD}_{HHMMSS}_{story_id}_{type}_{title}.md`

## Notes

- Chinese language output is expected for insights
- The `opencode` CLI tool is used for AI summarization
- Beijing timezone (UTC+8) is used for timestamps
- Always use `encoding="utf-8"` when reading/writing files with Chinese content