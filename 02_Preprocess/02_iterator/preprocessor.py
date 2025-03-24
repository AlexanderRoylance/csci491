import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def preprocess_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Convert to lowercase, remove special characters, remove stopwords
    text = re.sub(r"[^a-zA-Z\s]", "", text.lower())
    text = " ".join(word for word in text.split() if word not in stop_words)

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(text)

# Usage
preprocess_text("scraped_text.txt", "preprocessed_text.txt")
