import openai
import json

# Ensure you have the latest OpenAI API key set in your environment
openai.api_key = ""
# Read the preprocessed text
with open("../01_input/preprocessed_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Define prompts for extraction
prompts = {
    "hero": "Extract words and phrases that portray the target as a hero in this text.",
    "victim": "Extract words and phrases that depict the target as a victim in this text.",
    "villain": "Extract words and phrases that describe an attacker as a villain in this text."
}

# Dictionary to store results
risk_language = {}

for category, prompt in prompts.items():
    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an NLP model extracting linguistic features."},
                  {"role": "user", "content": f"{prompt}\n\n{text}"}]
    )
    
    extracted_words = response['choices'][0]['message']['content'].strip().split(", ")
    risk_language[category] = extracted_words

with open("risk_language_summary.json", "w", encoding="utf-8") as f:
    json.dump(risk_language, f, indent=4)

# Also save each category as a separate text file
for category in ["hero", "victim", "villain"]:
    with open(f"../03_output/{category}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(risk_language[category]))

print("Extraction complete. Files saved: risk_language_summary.json, hero.txt, victim.txt, villain.txt")


