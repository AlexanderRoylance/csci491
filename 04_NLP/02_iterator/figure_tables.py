import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Input file path
INPUT_FILE = "../03_output/tfidf_scores.csv"

# Read the TF-IDF scores
df = pd.read_csv(INPUT_FILE)

# Set plot style
sns.set(style="whitegrid")

# Function to create and display a barplot
def plot_top_terms(data, title, top_n=20):
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data.head(top_n), x="score", y="term", palette="viridis")
    plt.title(title)
    plt.xlabel("TF-IDF Score")
    plt.ylabel("Term")
    plt.tight_layout()
    plt.show()

# Plot top unigrams
unigrams = df[df["ngram_type"] == "unigram"].sort_values(by="score", ascending=False)
plot_top_terms(unigrams, "Top Unigrams by TF-IDF Score")

# Plot top bigrams
bigrams = df[df["ngram_type"] == "bigram"].sort_values(by="score", ascending=False)
plot_top_terms(bigrams, "Top Bigrams by TF-IDF Score")

# Plot top trigrams
trigrams = df[df["ngram_type"] == "trigram"].sort_values(by="score", ascending=False)
plot_top_terms(trigrams, "Top Trigrams by TF-IDF Score")

# Plot top overall terms
top_all = df.sort_values(by="score", ascending=False)
plot_top_terms(top_all, "Top Overall N-grams by TF-IDF Score")

#Sentiment Analysis
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
visualize_sentiment("../03_output/sentiment_scores.csv")
