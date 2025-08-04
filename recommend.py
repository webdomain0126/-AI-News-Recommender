# src/recommend.py

import json
import re

def load_articles(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def recommend_articles(articles, user_keywords, top_n=5):
    recommended = []

    for article in articles:
        combined_text = (article.get('title', '') + ' ' + article.get('summary', '')).lower()
        score = sum(1 for kw in user_keywords if re.search(rf"\b{re.escape(kw.lower())}\b", combined_text))
        if score > 0:
            article['match_score'] = score
            recommended.append(article)

    # Sort by match score
    recommended = sorted(recommended, key=lambda x: x['match_score'], reverse=True)
    return recommended[:top_n]

# Test
if __name__ == "__main__":
    user_keywords = ["AI", "healthcare", "robotics", "finance"]
    articles = load_articles("output/processed_results.json")

    recommendations = recommend_articles(articles, user_keywords)
    
    for idx, article in enumerate(recommendations, 1):
        print(f"\n🔹 Recommendation #{idx}")
        print(f"Title: {article['title']}")
        print(f"Summary: {article['summary']}")
        print(f"Match Score: {article['match_score']}")
