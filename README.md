# 📖 Diary Tone Analyzer

A simple web app built with **Streamlit**, **NLTK**, and **Plotly** that analyzes the emotional tone of your daily diary entries. It visualizes how positive or negative your mood is over time.

---

## 🔍 Features

- Uses NLTK's VADER sentiment analyzer to detect sentiment
- Displays interactive line charts showing:
  - **Positivity** trends
  - **Negativity** trends

---

## ✅ Requirements

- Python 3.9+
- `nltk`
- `plotly`
- `streamlit`

### Install dependencies:

```bash
pip install nltk plotly streamlit
```

## 📥 Download NLTK resources:

```bash
import nltk
nltk.download('vader_lexicon')
```

## 🚀 Running the App

Use the terminal to run the Streamlit app:
```bash
streamlit run main.py
```

The app will open automatically in your default browser.
