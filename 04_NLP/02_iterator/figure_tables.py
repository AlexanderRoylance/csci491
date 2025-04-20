import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
import re

# Set plot style
sns.set(style="whitegrid")

# --------------------------
# TF-IDF Visualizations
# --------------------------

INPUT_FILE = "../03_output/tfidf_scores.csv"
df = pd.read_csv(INPUT_FILE)

# Define keywords for highlighting
HERO_KEYWORDS = [
    "warning signs", "help"
]
VILLAIN_KEYWORDS = [
    "scams", "scam", "scammers", "fraud"
]
VICTIM_KEYWORDS = [
    "older adults", "adults", "seniors"
]

def plot_top_terms(data, title, top_n=20):
    # Select top terms
    plot_data = data.head(top_n).copy()

    # Assign color using consistent scheme
    def get_color(term):
        if any(keyword in term for keyword in HERO_KEYWORDS):
            return "green"
        elif any(keyword in term for keyword in VILLAIN_KEYWORDS):
            return "red"
        elif any(keyword in term for keyword in VICTIM_KEYWORDS):
            return "blue"
        else:
            return "gray"

    plot_data["color"] = plot_data["term"].apply(get_color)

    # Plot
    plt.figure(figsize=(12, 6))
    for i, row in plot_data.iterrows():
        plt.bar(
            row["term"],
            row["score"],
            color=row["color"],           # fill color with default opacity
            edgecolor=row["color"],      # border color
            linewidth=2,
            alpha=0.3                    # semi-transparent fill
        )

    plt.title(title)
    plt.ylabel("TF-IDF Score")
    plt.xlabel("Term")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 0.6)
    plt.tight_layout()
    plt.show()



# Filter by n-gram type and plot
unigrams = df[df["ngram_type"] == "unigram"].sort_values(by="score", ascending=False)
plot_top_terms(unigrams, "Top Unigrams by TF-IDF Score")

bigrams = df[df["ngram_type"] == "bigram"].sort_values(by="score", ascending=False)
plot_top_terms(bigrams, "Top Bigrams by TF-IDF Score")

trigrams = df[df["ngram_type"] == "trigram"].sort_values(by="score", ascending=False)
plot_top_terms(trigrams, "Top Trigrams by TF-IDF Score")

top_all = df.sort_values(by="score", ascending=False)
plot_top_terms(top_all, "Top Overall N-grams by TF-IDF Score")

# --------------------------
# Sentiment Analysis
# --------------------------

def visualize_sentiment(sentiment_file):
    df = pd.read_csv(sentiment_file)

    df = df[df["Word"].str.contains(" ") == False]
    df["Category"] = df["Category"].str.strip().str.lower()
    df = df.drop_duplicates(subset=["Word", "Category"])

    df_sorted = df.sort_values(by="Sentiment Score")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df_sorted, x="Word", y="Sentiment Score", hue="Category", dodge=False)
    plt.xticks(rotation=90)
    plt.title("Sentiment Scores of Unique Single Words (Sorted)")
    plt.xlabel("Words")
    plt.ylabel("Sentiment Score")
    plt.axhline(0, color="black", linewidth=1)
    plt.tight_layout()
    plt.show()

    categories = ['hero', 'villain', 'victim']
    for cat in categories:
        subset = df[df["Category"] == cat].copy()
        if subset.empty:
            print(f"No data for category: {cat}")
            continue

        subset["score_bin"] = subset["Sentiment Score"].round(2)
        subset["y_pos"] = subset.groupby("score_bin").cumcount()

        fig = px.scatter(
            subset,
            x="Sentiment Score",
            y="y_pos",
            hover_data=["Word", "Sentiment Score"],
            title=f"Sentiment Distribution Stack for {cat.capitalize()}",
            color_discrete_sequence=["green" if cat == "hero" else "red" if cat == "villain" else "blue"]
        )

        fig.update_traces(marker=dict(size=10, opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
        fig.update_layout(
            yaxis=dict(title="", showticklabels=False),
            xaxis=dict(title="Sentiment Score"),
            showlegend=False,
            height=400 + subset["y_pos"].max() * 10
        )
        fig.show()

    plt.figure(figsize=(12, 6))
    for cat in categories:
        subset = df[df["Category"] == cat]
        if subset.empty:
            continue
        sns.kdeplot(subset["Sentiment Score"], label=cat.capitalize(), fill=True, alpha=0.3)
    plt.title("Distribution of Sentiment Scores by Category")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Density")
    plt.axvline(0, color="black", linestyle="--")
    plt.legend()
    plt.tight_layout()
    plt.show()

# --------------------------
# Word Complexity Analysis
# --------------------------

def analyze_word_complexity(text_folder):
    categories = ['hero', 'villain', 'victim']
    all_words = []

    for cat in categories:
        with open(f"{text_folder}/{cat}.txt", "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            for word in words:
                all_words.append({"Word": word, "Length": len(word), "Category": cat})

    df = pd.DataFrame(all_words)

    # --- Graph 1: Word Complexity by Category ---
    plt.figure(figsize=(12, 6))
    sns.kdeplot(data=df, x="Length", hue="Category", fill=True, common_norm=False, alpha=0.4)
    plt.title("Word Complexity (Length) by Category")
    plt.xlabel("Word Length")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()

    # --- Graph 2: Combined Complexity Distribution ---
    plt.figure(figsize=(10, 5))
    sns.kdeplot(data=df, x="Length", fill=True, color="purple", alpha=0.4)
    plt.title("Overall Word Complexity Distribution")
    plt.xlabel("Word Length")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()

# --------------------------
# Run Everything
# --------------------------

visualize_sentiment("../03_output/sentiment_scores.csv")
analyze_word_complexity("../01_input")
