import openai
import json

# Ensure you have the latest OpenAI API key set in your environment
openai.api_key = ""
# Read the preprocessed text
with open("../01_input/preprocessed_text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Define prompts for extraction
prompts = {
    "hero": "Extract Sentences that demonstrate Individuals or entities that try to help, prevent, or resolve the phishing attack. do not say anything other than these sentences.(no numbers no explanation)",
    "victim": "Extract Sentences that portray Individuals or entities who were deceived or harmed by the phishing attack. do not say anything other than these sentences.(no numbers no explanation)",
    "villain": "Extract Sentences that describe Perpetrators of the phishing attack (e.g., scammers, fraudsters). do not say anything other than these sentences (no numbers no explanation)."
}

# Dictionary to store results
risk_language = {}

for category, prompt in prompts.items():
    response = openai.chat.completions.create( 
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an NLP model extracting linguistic features."},
                  {"role": "user", "content": f"{prompt}\n\n{text}"}]
    )
    
    extracted_words = response.choices[0].message.content.strip().split(".")
    risk_language[category] = extracted_words

with open("risk_language_summary.json", "w", encoding="utf-8") as f:
    json.dump(risk_language, f, indent=4)

# Also save each category as a separate text file
for category in ["hero", "victim", "villain"]:
    with open(f"../03_output/{category}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(risk_language[category]))

print("Extraction complete. Files saved: risk_language_summary.json, hero.txt, victim.txt, villain.txt")


