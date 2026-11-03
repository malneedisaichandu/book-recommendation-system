# Book Recommendation System

A simple web app that recommends books based on the genre of a favourite book using TF-IDF and cosine similarity.

## Overview
This project uses a book dataset and compares book genres to find similar titles. It is built with Python and Streamlit, making it easy to run locally in a browser.

## Features
- Search for a favourite book by name
- Recommend the top 5 similar books
- Uses TF-IDF vectorization on the `Genre` field
- Calculates similarity using cosine similarity
- Lightweight and beginner-friendly project

## Tech Stack
- Python
- Streamlit
- Pandas
- scikit-learn

## Project Structure
- `app.py` — Streamlit app logic
- `Book_Recommendation_Dataset.csv` — book dataset
- `requirements.txt` — Python dependencies
- `Steps.txt` — quick run instructions

## Installation
1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv myvenv
```

On Windows:

```bash
myvenv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App
```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## How It Works
- The app reads the dataset from `Book_Recommendation_Dataset.csv`
- It converts each book's genre into TF-IDF features
- It computes similarity scores between books
- When a user enters a book name, the app shows the most similar books

## Example
If the user enters a title such as "The Alchemist", the app will suggest other books with similar genres.

## License
This project is for educational and personal use.

## Author
Created as a simple book recommendation project for learning and demonstration.
