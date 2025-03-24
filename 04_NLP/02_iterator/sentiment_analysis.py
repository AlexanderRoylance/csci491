from textblob import TextBlob
import pandas as pd

def analyze_sentiment(input_files, output_file):
    sentiment_data = []

    for file in input_files:
        with open(file, "r", encoding="utf-8") as f:
            words = f.read().split()

        for word in words:
            polarity = TextBlob(word).sentiment.polarity
            if polarity != 0:  # Filter out neutral words
                sentiment_data.append({"Word": word, "Sentiment Score": polarity, "Category": file.split(".")[0]})

    # Save sentiment scores to a CSV file
    df = pd.DataFrame(sentiment_data)
    df.to_csv(output_file, index=False)
    print(f"Sentiment scores saved to {output_file}")

# Usage
input_files = ["../01_input/hero.txt", "../01_input/victim.txt", "../01_input/villain.txt"]
analyze_sentiment(input_files, "sentiment_scores.csv")