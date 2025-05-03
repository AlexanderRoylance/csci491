# Risk Communication Message Analysis Pipeline

This project analyzes digital risk communication messages targeted at older adults, aiming to improve their clarity, emotional tone, and effectiveness using a structured NLP pipeline. The analysis is grounded in the Narrative Policy Framework and includes TF-IDF scoring, sentiment analysis, word complexity scoring, and custom message generation.

## 🔍 Overview

Scammers are increasingly targeting older populations through deceptive digital means. Many existing messages use complex or negative language that may reduce their effectiveness. Our goal is to identify linguistic weaknesses and strengths in current messaging and generate simplified, emotionally resonant alternatives.

---

## Pipeline Structure

### 1. Input Collection
- Accepts a file of URLs containing risk communication messages.
- Extracts raw text from each webpage using a web scraping module.

### 2. Text Preprocessing
- Converts text to lowercase.
- Removes special characters and stopwords.
- Outputs a cleaned corpus for analysis.

### 3. Narrative Role Extraction
- Applies the **Narrative Policy Framework** to categorize words into:
  - **Hero**
  - **Victim**
  - **Villain**
- Extracted words are stored in separate JSON or text files.

### 4. NLP
### TF-IDF Analysis
- Calculates term frequency–inverse document frequency scores.
- Identifies most salient unigrams and bigrams for each narrative role.
- Outputs TF-IDF tables for comparative analysis.

### Sentiment Analysis
- Assigns sentiment polarity scores to words in each category.
- Highlights emotionally charged language.
- Generates sentiment distribution plots by narrative role.

### Word Complexity Analysis
- Uses two methods:
  - **Age of Acquisition (AoA)** scores from psycholinguistic data.
  - **LLM-based difficulty rating (1–5)** based on length and semantics.
- Detects bimodal distributions and identifies overly complex terms.

### 5. Message Generation
- Combines simplest and most emotionally extreme words for each narrative role.
- Generates new, easy-to-understand, emotionally resonant risk messages.
- Output includes:
  - 1–4 sentence messages.
  - Breakdown of word types and sentiment scores.

### 6. Analysis
- Compare generated and original messages
- dislplay graphs detailing findings
