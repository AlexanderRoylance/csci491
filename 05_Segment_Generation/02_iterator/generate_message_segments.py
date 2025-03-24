import json
import openai

# Load the risk language summary
def load_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Generate a message segment using OpenAI API
def generate_segment(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Generate a short risk communication message segment."},
                  {"role": "user", "content": prompt}],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"].strip()

# Main function
def generate_messages(summary_file, output_file):
    summary = load_summary(summary_file)

    hero_prompt = f"Create a brief motivational message for elderly users using these words: {', '.join(summary['hero_language'])}."
    victim_prompt = f"Create a warning message that highlights potential dangers using: {', '.join(summary['victim_language'])}."
    villain_prompt = f"Create a message that exposes phishing threats using: {', '.join(summary['villain_language'])}."

    hero_segment = generate_segment(hero_prompt)
    victim_segment = generate_segment(victim_prompt)
    villain_segment = generate_segment(villain_prompt)

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Hero: {hero_segment}\n")
        f.write(f"Victim: {victim_segment}\n")
        f.write(f"Villain: {villain_segment}\n")

    print(f"Generated segments saved to {output_file}")

# Usage
generate_messages("../01_input/risk_language_summary.json", "../03_output/generated_segments.txt")
