from textblob import TextBlob
import pandas as pd

def analyze_sentiment(input_files, output_file):
    sentiment_data = []
    seen_phrases = set()  # Use a set to track unique phrases

    for file in input_files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read().lower()  # Convert to lowercase

        category = file.split("/")[-1].rsplit(".", 1)[0]  # Extract category name

        # Tokenize into sentences
        blob = TextBlob(text)
        
        for sentence in blob.sentences:
            sentence_polarity = sentence.sentiment.polarity  # Get overall sentence sentiment
            words = [word.strip(",.!?()[]{}\"'") for word in sentence.words]  # Clean punctuation
            words = [word for word in words if word]  # Remove empty words

            # Extract unigrams (single words)
            for word in words:
                word_polarity = TextBlob(word).sentiment.polarity
                
                # If the word alone has no sentiment, inherit from the sentence
                if word_polarity == 0:
                    word_polarity = sentence_polarity
                
                if word not in seen_phrases and word_polarity != 0:
                    sentiment_data.append({
                        "Word": word,
                        "Sentiment Score": word_polarity,
                        "Category": category
                    })
                    seen_phrases.add(word)

            # Extract bigrams (two-word phrases) and trigrams (three-word phrases)
            for n in [2, 3]:
                ngrams = zip(*[words[i:] for i in range(n)])
                for phrase in ngrams:
                    phrase_text = " ".join(phrase)
                    phrase_polarity = TextBlob(phrase_text).sentiment.polarity
                    
                    # If the phrase alone has no sentiment, inherit from the sentence
                    if phrase_polarity == 0:
                        phrase_polarity = sentence_polarity
                    
                    if phrase_text not in seen_phrases and phrase_polarity != 0:
                        sentiment_data.append({
                            "Word": phrase_text,
                            "Sentiment Score": phrase_polarity,
                            "Category": category
                        })
                        seen_phrases.add(phrase_text)

    # Save sentiment scores to a CSV file
    df = pd.DataFrame(sentiment_data)
    df.to_csv(output_file, index=False)
    print(f"Sentiment scores saved to {output_file}")

# Usage
input_files = ["../01_input/hero.txt", "../01_input/victim.txt", "../01_input/villain.txt"]
analyze_sentiment(input_files, "../03_output/sentiment_scores.csv")
