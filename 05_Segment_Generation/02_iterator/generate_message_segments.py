import json
import openai
import pandas as pd
import os

# Set your OpenAI API key
openai.api_key = ""

# Load summary JSON if needed
def load_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Get top TF-IDF terms based on sentiment
def get_top_terms(tfidf_path, sentiment_path, category, top_n=8):
    tfidf_df = pd.read_csv(tfidf_path)
    sentiment_df = pd.read_csv(sentiment_path)

    tfidf_df.columns = tfidf_df.columns.str.strip()
    sentiment_df.columns = sentiment_df.columns.str.strip()

    merged = tfidf_df.merge(sentiment_df, left_on='term', right_on='Word')
    filtered = merged[merged['Category'].str.lower() == category.lower()]
    sorted_terms = filtered.sort_values(by='score', ascending=False)['term'].drop_duplicates()

    return sorted_terms.head(top_n).tolist()

# Generate one segment
def generate_segment(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Generate a short risk communication message segment."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60
    )
    return response.choices[0].message.content.strip()

# Save multiple segments to file
def save_segments(file_path, prompt, num_segments=3):
    with open(file_path, "w", encoding="utf-8") as f:
        for _ in range(num_segments):
            f.write(f"- {generate_segment(prompt)}\n")
    print(f"Wrote {num_segments} segments to {file_path}")

# Main generator
def generate_messages(summary_file, output_dir, tfidf_file, sentiment_file, num_segments=3):
    os.makedirs(output_dir, exist_ok=True)
    _ = load_summary(summary_file)

    # Get keywords
    top_hero_terms = ', '.join(get_top_terms(tfidf_file, sentiment_file, "Hero"))
    top_victim_terms = ', '.join(get_top_terms(tfidf_file, sentiment_file, "Victim"))
    top_villain_terms = ', '.join(get_top_terms(tfidf_file, sentiment_file, "Villain"))

    # Main prompts
    hero_prompt = (
        f"Create a brief motivational message (1-2 sentences) for elderly users to empower and reassure them in avoiding online threats. "
        f"Include important terms: {top_hero_terms}. Use emotionally uplifting language. Tone: warm, supportive, proactive."
    )
    victim_prompt = (
        f"Create a short warning message (1-2 sentences) for elderly users about phishing dangers. "
        f"Include important terms: {top_victim_terms}. Use emotionally serious or fearful language. Tone: cautious and protective."
    )
    villain_prompt = (
        f"Create a brief message (1-2 sentences) that identifies phishing attackers and their behavior. "
        f"Include important terms: {top_villain_terms}. Use emotionally negative or dangerous language. Tone: assertive and critical."
    )

    # Prevention prompts
    hero_prevention_prompt = (
        "Create a short phishing prevention message (1-2 sentences) that empowers elderly users to protect themselves. "
        "Use confident, proactive tone. Emphasize smart habits like checking links or trusting instincts."
    )
    victim_prevention_prompt = (
        "Create a short phishing prevention warning (1-2 sentences) that helps elderly users avoid being tricked. "
        "Use cautious, serious tone. Emphasize how scammers create urgency or fake trust."
    )
    villain_prevention_prompt = (
        "Create a short phishing prevention message (1-2 sentences) that explains how attackers behave and how to detect them. "
        "Use assertive tone. Mention common tricks like fake login pages, spoofed caller IDs, or urgent messages."
    )

    # Save outputs
    save_segments(os.path.join(output_dir, "hero_messages.txt"), hero_prompt, num_segments)
    save_segments(os.path.join(output_dir, "victim_messages.txt"), victim_prompt, num_segments)
    save_segments(os.path.join(output_dir, "villain_messages.txt"), villain_prompt, num_segments)

    save_segments(os.path.join(output_dir, "hero_prevention.txt"), hero_prevention_prompt, num_segments)
    save_segments(os.path.join(output_dir, "victim_prevention.txt"), victim_prevention_prompt, num_segments)
    save_segments(os.path.join(output_dir, "villain_prevention.txt"), villain_prevention_prompt, num_segments)

# === RUN ===
generate_messages(
    summary_file="../01_input/risk_language_summary.json",
    output_dir="../03_output/",
    tfidf_file="../../04_NLP/03_output/tfidf_scores.csv",
    sentiment_file="../../04_NLP/03_output/sentiment_scores.csv",
    num_segments=3
)
