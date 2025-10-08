# ====================================================
# 🎵 SONG LYRICS EMOTION ANALYZER — STREAMLIT VERSION
# ====================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(page_title="🎵 Song Lyrics Emotion Analyzer", layout="centered")

# -----------------------------
# LOAD MODELS
# -----------------------------
@st.cache_resource
def load_models():
    # Load emotion classification model
    emotion_model = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
        framework="pt"
    )
    # Download VADER
    nltk.download('vader_lexicon', quiet=True)
    sentiment_analyzer = SentimentIntensityAnalyzer()
    return emotion_model, sentiment_analyzer

emotion_classifier, sentiment_analyzer = load_models()

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("🎵 Song Lyrics Emotion Analyzer")
st.write("Analyze your song lyrics for emotions and sentiment using AI 🎭")

lyrics = st.text_area("Paste your lyrics below 👇", height=200,
                      placeholder="Type or paste song lyrics here...")

# Possible emotions (you can modify these)
emotion_labels = ["love", "joy", "sadness", "anger", "fear", "surprise"]

# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("🔍 Analyze Emotion"):
    if not lyrics.strip():
        st.warning("Please enter some lyrics first.")
    else:
        with st.spinner("Analyzing emotions... ⏳"):
            result = emotion_classifier(lyrics, emotion_labels)
            scores = dict(zip(result["labels"], result["scores"]))
            sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

        # -----------------------------
        # DISPLAY EMOTION RESULTS
        # -----------------------------
        top_emotion = max(sorted_scores, key=sorted_scores.get)
        confidence = sorted_scores[top_emotion] * 100

        st.subheader(f"🎭 Predicted Emotion: **{top_emotion.upper()} ({confidence:.2f}%)**")

        df = pd.DataFrame({
            "Emotion": list(sorted_scores.keys()),
            "Score (%)": [round(v * 100, 2) for v in sorted_scores.values()]
        })

        # Bar Chart
        st.bar_chart(df.set_index("Emotion"))

        # Pie Chart
        fig, ax = plt.subplots()
        ax.pie(df["Score (%)"], labels=df["Emotion"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        # -----------------------------
        # SENTIMENT POLARITY (VADER)
        # -----------------------------
        sentiment = sentiment_analyzer.polarity_scores(lyrics)
        if sentiment["compound"] > 0:
            sentiment_label = "Positive 😊"
        elif sentiment["compound"] < 0:
            sentiment_label = "Negative 😔"
        else:
            sentiment_label = "Neutral 😐"

        st.subheader(f"🧭 Overall Sentiment: {sentiment_label}")
        st.write(sentiment)

st.markdown("---")
st.caption("Developed by Ishan Jain | Text Mining Project 2025")
