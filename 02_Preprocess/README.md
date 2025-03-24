
**File:** `preprocess/README.md`  

# Preprocessing Module

## Overview
This module processes raw scraped text by:
- Converting text to lowercase
- Removing special characters
- Removing stopwords

## Input
- `scraped_text.txt` → The raw text from the scraper.

## Output
- `preprocessed_text.txt` → Cleaned text for analysis.

## Usage
Run the following command:
```bash
python preprocess.py scraped_text.txt preprocessed_text.txt
