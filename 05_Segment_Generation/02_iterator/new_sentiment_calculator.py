import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from collections import Counter
import re

# Set plot style
sns.set(style="whitegrid")

# --------------------------
# Sentiment Analysis
# --------------------------

def visualize_sentiment(sentiment_file):
    df = pd.read_csv(sentiment_file)

    # Keep only single words
    df = df[df["Word"].str.contains(" ") == False]

    # Normalize and extract base category
    df["Category"] = df["Category"].str.extract(r'(hero|villain|victim)', expand=False).str.lower()
    df = df.dropna(subset=["Category"])
    df = df.drop_duplicates(subset=["Word", "Category"])

    # Barplot of unique single words sorted by sentiment score
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

    # Plot stacked sentiment dots by category using Plotly
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

    # KDE Plot for sentiment score distribution
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
# Run Everything
# --------------------------

visualize_sentiment("../03_output/new_sentiment_scores.csv")
