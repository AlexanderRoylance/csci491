import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Load sentiment scores
def load_sentiment_data(sentiment_file):
    df = pd.read_csv(sentiment_file)
    return {row["Word"]: row["Sentiment Score"] for _, row in df.iterrows()}

# Load generated segments
def load_segments(segment_file):
    with open(segment_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {line.split(":")[0]: line.split(":")[1].strip() for line in lines}

# Color-coding function
def get_category_color(word, summary):
    if word in summary["hero_language"]:
        return "blue"
    elif word in summary["victim_language"]:
        return "red"
    elif word in summary["villain_language"]:
        return "green"
    return "gray"  # Default color for unknown words

# Visualization
def plot_sentiment(segments, sentiment_data, summary):
    for category, text in segments.items():
        words = text.split()
        sentiment_scores = [sentiment_data.get(word, 0) for word in words]
        colors = [get_category_color(word, summary) for word in words]

        plt.figure(figsize=(10, 6))
        sns.barplot(x=words, y=sentiment_scores, palette=colors)
        plt.xticks(rotation=45)
        plt.title(f"Sentiment Analysis for {category} Segment")
        plt.xlabel("Words")
        plt.ylabel("Sentiment Score")
        plt.axhline(0, color="black", linewidth=1)  # Neutral sentiment line
        plt.show()

# Main function
def analyze_segments(segment_file, sentiment_file, summary_file):
    sentiment_data = load_sentiment_data(sentiment_file)
    segments = load_segments(segment_file)

    with open(summary_file, "r", encoding="utf-8") as f:
        summary = json.load(f)

    plot_sentiment(segments, sentiment_data, summary)

# Usage
analyze_segments("../01_input/generated_segments.txt", "../01_input/sentiment_scores.csv", "../01_input/risk_language_summary.json")
