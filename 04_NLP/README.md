
# NLP Analysis Module

## Overview
This module performs:
- **TF-IDF Analysis** (to identify important words and bigrams).
- **Sentiment Analysis** (to evaluate emotional tone).

## Input
- `hero.txt`
- `victim.txt`
- `villain.txt`

## Output
- `tfidf_scores.csv` → TF-IDF scores.
- `sentiment_scores.csv` → Sentiment scores.

## Usage
Run the following commands:
```bash
python tfidf_analysis.py hero.txt victim.txt villain.txt tfidf_scores.csv
python sentiment_analysis.py hero.txt victim.txt villain.txt sentiment_scores.csv
