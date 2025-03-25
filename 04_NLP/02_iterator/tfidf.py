from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def compute_tfidf(input_files, output_file):
    texts = [open(f, "r", encoding="utf-8").read() for f in input_files]
    vectorizer = TfidfVectorizer(ngram_range=(1,2))  # Single words & bigrams
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    feature_names = vectorizer.get_feature_names_out()
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names, index=[f.split(".")[0] for f in input_files])
    
    # Save TF-IDF scores to a CSV file
    tfidf_df.to_csv(output_file)
    print(f"TF-IDF scores saved to {output_file}")

# Usage
input_files = ["../../03_Operationalization/01_input/preprocessed_text.txt"]
compute_tfidf(input_files, "../03_output/tfidf_scores.csv")
