import openai

openai.api_key = "YOUR_API_KEY"

def extract_language(input_file, output_files, categories):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    
    for category, output_file in zip(categories, output_files):
        prompt = f"Extract all words and phrases related to '{category}' language in this text:\n\n{text}"
        
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        extracted_text = response["choices"][0]["message"]["content"]

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(extracted_text)

# Usage
categories = ["hero", "victim", "villain"]
output_files = ["hero.txt", "victim.txt", "villain.txt"]
extract_language("preprocessed_text.txt", output_files, categories)

