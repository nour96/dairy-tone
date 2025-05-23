import glob
import streamlit as st
import plotly.express as px
import nltk 
nltk.download("vader_lexicon")

from nltk.sentiment import SentimentIntensityAnalyzer


filepaths = sorted(glob.glob("diary/*.txt"))
analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    positivity.append(scores["pos"])
    negativity.append(scores["neg"])
    
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y":"Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y":"Negativity"})
st.plotly_chart(neg_figure)