import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pathlib import Path

# File paths
INPUT_FILE = "../../03_Operationalization/01_input/preprocessed_text.txt"
OUTPUT_FILE = "../03_output/tfidf_scores.csv"

# Read the input text
with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    text = file.read()

# Split into a list of one document (in case needed later for multi-docs)
documents = [text]

# Function to compute TF-IDF for given n-gram range
def compute_tfidf(documents, ngram_range):
    vectorizer = TfidfVectorizer(ngram_range=ngram_range)
    tfidf_matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray().flatten()
    return pd.DataFrame({"term": feature_names, "score": scores})

# Compute TF-IDF for unigrams, bigrams, trigrams
unigrams_df = compute_tfidf(documents, (1, 1))
bigrams_df = compute_tfidf(documents, (2, 2))
trigrams_df = compute_tfidf(documents, (3, 3))

# Sort each by score
unigrams_df = unigrams_df.sort_values(by="score", ascending=False)
bigrams_df = bigrams_df.sort_values(by="score", ascending=False)
trigrams_df = trigrams_df.sort_values(by="score", ascending=False)

# Add ngram type labels
unigrams_df["ngram_type"] = "unigram"
bigrams_df["ngram_type"] = "bigram"
trigrams_df["ngram_type"] = "trigram"

# Combine and reorder columns
combined_df = pd.concat([unigrams_df, bigrams_df, trigrams_df], ignore_index=True)
combined_df = combined_df[["ngram_type", "term", "score"]]

# Ensure output directory exists
Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

# Save to CSV
combined_df.to_csv(OUTPUT_FILE, index=False)

print(f"TF-IDF scores saved to: {OUTPUT_FILE}")
