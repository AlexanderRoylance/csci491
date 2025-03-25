import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_tfidf(tfidf_file):
    df = pd.read_csv(tfidf_file, index_col=0)
    df = df.T  # Transpose for better readability

    print("TF-IDF Table Preview:")
    print(df.head(10))  # Display first 10 words

    plt.figure(figsize=(12, 6))
    sns.heatmap(df, cmap="Blues", linewidths=0.5, linecolor="gray")
    plt.title("TF-IDF Scores Across Documents")
    plt.xlabel("Document Category")
    plt.ylabel("Words/Bigrams")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.show()

def visualize_sentiment(sentiment_file):
    df = pd.read_csv(sentiment_file)
    
    # **Filter single words only (remove phrases)**
    df = df[df["Word"].str.contains(" ") == False]  # Keep words without spaces

    # **Drop duplicate words, keeping the first occurrence per category**
    df = df.drop_duplicates(subset=["Word", "Category"])

    # **Plot**
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="Word", y="Sentiment Score", hue="Category", dodge=False)
    plt.xticks(rotation=90)
    plt.title("Sentiment Scores of Unique Single Words")
    plt.xlabel("Words")
    plt.ylabel("Sentiment Score")
    plt.axhline(0, color="black", linewidth=1)  # Neutral sentiment line
    plt.show()

# Usage
visualize_tfidf("../03_output/tfidf_scores.csv")
visualize_sentiment("../03_output/sentiment_scores.csv")
