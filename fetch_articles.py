# src/fetch_articles.py

import json
import os

def load_articles():
    file_path = os.path.join("data", "sample_articles.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    try:
        articles = load_articles()
        print("✅ Articles loaded:\n")

        for i, article in enumerate(articles, 1):
            print(f"📄 Article {i}: {article['title']}\n{article['content'][:200]}...\n")

    except Exception as e:
        print(f"❌ Failed to load articles: {e}")
