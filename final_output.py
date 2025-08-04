import json

# Load all partial outputs
with open("output/processed_results.json", "r") as f:
    summaries = json.load(f)

with open("output/categorized_results.json", "r") as f:
    categories = json.load(f)

with open("output/read_times.json", "r") as f:
    read_times = json.load(f)

# Merge all fields based on title
final_results = []

for summary in summaries:
    title = summary["title"]
    item = {
        "title": title,
        "summary": summary["summary"],
        "sentiment": summary.get("sentiment", "N/A"),
        "category": "N/A",
        "read_time": "N/A"
    }

    for cat in categories:
        if cat["title"] == title:
            item["category"] = cat.get("category", "N/A")
            break

    item["read_time"] = read_times.get(title, "N/A")
    final_results.append(item)

# Save to JSON file
with open("output/final_results.json", "w") as f:
    json.dump(final_results, f, indent=4)

# Display pretty output
for i, article in enumerate(final_results, 1):
    print(f"\n📰 Article #{i}")
    print(f"Title: {article['title']}")
    print(f"📄 Summary: {article['summary']}")
    print(f"🕒 Read Time: {article['read_time']}")
    print(f"❤️ Sentiment: {article['sentiment']}")
    print(f"🏷️ Category: {article['category']}")
