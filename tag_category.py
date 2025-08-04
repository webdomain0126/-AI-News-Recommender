import json

# 1. Category keywords dictionary
category_keywords = {
    "Health": ["health", "medicine", "hospital", "covid", "vaccine"],
    "Finance": ["stock", "market", "economy", "finance", "crypto"],
    "Technology": ["AI", "robot", "technology", "software", "machine learning"],
    "Education": ["education", "school", "university", "student", "teacher"],
    "Environment": ["climate", "pollution", "environment", "earth", "sustainability"]
}

# 2. Assign category based on keywords
def assign_category(article, category_keywords):
    text = f"{article['title']} {article['summary']}".lower()
    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text:
                return category
    return "Other"

# 3. Load articles from JSON
def load_articles(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# 4. Save updated articles with category added
def save_articles(articles, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

# 5. Main program
if __name__ == "__main__":
    input_file = "output/processed_results.json"  # Your summarized articles
    output_file = "output/categorized_results.json"

    articles = load_articles(input_file)

    for article in articles:
        article["category"] = assign_category(article, category_keywords)

    save_articles(articles, output_file)
    print("✅ Category tagging complete. Saved to:", output_file)
