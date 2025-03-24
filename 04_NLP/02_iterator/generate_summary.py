import json
import pandas as pd

def generate_summary(tfidf_file, sentiment_file, hero_file, victim_file, villain_file, output_file):
    # Read sentiment scores
    sentiment_df = pd.read_csv(sentiment_file)
    sentiment_summary = sentiment_df.groupby("Category")["Sentiment Score"].agg(["mean"]).to_dict()["mean"]
    
    # Read TF-IDF scores
    tfidf_df = pd.read_csv(tfidf_file, index_col=0).T
    top_tfidf = {
        category: list(tfidf_df[category].nlargest(3).index) 
        for category in tfidf_df.columns
    }

    # Read extracted words
    def load_words(file):
        with open(file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]

    data = {
        "hero_language": load_words(hero_file),
        "victim_language": load_words(victim_file),
        "villain_language": load_words(villain_file),
        "top_tfidf_words": top_tfidf,
        "sentiment_summary": {
            category: {"positive": round(max(0, score), 2), "negative": round(abs(min(0, score)), 2)}
            for category, score in sentiment_summary.items()
        }
    }

    # Save structured output
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Summary saved to {output_file}")

# Usage
generate_summary("tfidf_scores.csv", "sentiment_scores.csv", "../01_input/hero.txt", "../01_input/victim.txt", "../01_input/villain.txt", "../03_output/risk_language_summary.json")