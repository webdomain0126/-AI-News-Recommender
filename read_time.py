import json
import os

# Load your processed results to calculate read times for their summaries
with open("output/processed_results.json", "r") as f:
    summaries = json.load(f)

def estimate_read_time(text, wpm=200):
    words = len(text.split())
    return max(1, round(words / wpm))

read_times = {}
for article in summaries:
    title = article["title"]
    summary_text = article["summary"]
    read_times[title] = estimate_read_time(summary_text)

os.makedirs("output", exist_ok=True)

with open("output/read_times.json", "w") as f:
    json.dump(read_times, f, indent=4)

print("✅ Created read_times.json successfully!")
