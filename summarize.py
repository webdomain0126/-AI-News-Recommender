# src/summarize.py

from transformers import pipeline

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_len=120):
    try:
        summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"⚠️ Summarization failed: {e}"

# Optional test run
if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence is transforming the way medical professionals diagnose diseases. "
        "Using advanced machine learning algorithms, these tools analyze vast datasets, often detecting patterns that are invisible to the human eye..."
    )

    print("📄 Original Text:")
    print(sample_text)
    print("\n✂️ Summary:")
    print(summarize_text(sample_text))
