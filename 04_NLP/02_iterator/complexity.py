import os
import openai
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from time import sleep

# Set your OpenAI API key (use environment variable for security)
openai.api_key = ""

# Files and categories
FILES = {
    "hero": "../01_input/hero.txt",
    "villain": "../01_input/villain.txt",
    "victim": "../01_input/victim.txt"
}

# Extract words from text
def extract_words(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return list(set(words))  # Unique words

# Call GPT to rate complexity from 1 (simple) to 5 (complex)
def get_complexity_rating(word):
    try:
        prompt = (
    f"On a scale from 1.0 (very simple) to 5.0 (very complex), "
    f"how complex is the word '{word}' in terms of readability and cognitive load? "
    f"Respond with only the number as a decimal between 1.0 and 5.0."
)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        rating = float(content)
        return rating
    except Exception as e:
        print(f"Error for word '{word}': {e}")
        return None

# Collect complexity data
all_data = []

for category, file in FILES.items():
    print(f"Processing {category}...")
    words = extract_words(file)
    for word in words:
        rating = get_complexity_rating(word)
        if rating:
            all_data.append({
                "Word": word,
                "Complexity": rating,
                "Category": category
            })
        sleep(0.5)  # Avoid hitting rate limits

# Create DataFrame
df = pd.DataFrame(all_data)
df.to_csv("word_complexity_results.csv", index=False)

# Plot results
plt.figure(figsize=(12, 6))
sns.kdeplot(data=df, x="Complexity", hue="Category", fill=True, common_norm=False, alpha=0.4)
plt.title("Word Complexity Distribution by Category")
plt.xlabel("GPT-Rated Complexity (1 = Simple, 5 = Complex)")
plt.ylabel("Density")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.show()
