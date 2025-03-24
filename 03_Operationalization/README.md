
# Character Word Extraction Module

## Overview
This module extracts "Hero," "Victim," and "Villain" language using OpenAI's API.

## Input
- `preprocessed_text.txt` → Cleaned text.

## Output
- `risk_language_summary.json` → A JSON file categorizing words into hero, victim, and villain.
- `hero.txt` → Words painting the target as a hero.
- `victim.txt` → Words portraying vulnerability.
- `villain.txt` → Words describing attackers.

## Usage
Run the following command:
```bash
python extract_language.py preprocessed_text.txt risk_language_summary.json
