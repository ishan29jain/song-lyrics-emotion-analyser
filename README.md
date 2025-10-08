# 🎵 Song Lyrics Emotion Analyzer

A **Text Mining + NLP project** that analyzes the **emotions and sentiment** present in song lyrics using **Zero-Shot Classification (BART-Large-MNLI)** and **VADER Sentiment Analysis**.  
Built with **Streamlit** for an interactive and elegant frontend.

---

## 🧠 Overview

The **Song Lyrics Emotion Analyzer** allows users to input any song lyric and instantly visualize:
- 🎭 **Predicted emotion** (love, joy, sadness, anger, fear, surprise)  
- 📊 **Emotion probability distribution** (bar & pie charts)  
- 🧭 **Overall sentiment** (positive, negative, or neutral)

This project combines **state-of-the-art NLP models** with an intuitive user interface to explore the hidden emotions behind lyrical language.

---

## 🚀 Features

✅ Zero-shot emotion detection using **`facebook/bart-large-mnli`**  
✅ Sentiment polarity detection via **VADER**  
✅ Interactive **Streamlit dashboard**  
✅ Real-time **bar and pie chart visualizations**  
✅ Easy deployment and lightweight architecture  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3 |
| Framework | Streamlit |
| NLP Model | `facebook/bart-large-mnli` (Hugging Face Transformers) |
| Sentiment Model | VADER (NLTK) |
| Visualization | Matplotlib, Streamlit Charts |

---

## 📁 Project Structure
```
song-lyrics-emotion-analyzer/
│
├── app.py # Streamlit app
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── sample_lyrics.txt # (Optional) Test data file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/song-lyrics-emotion-analyzer.git
cd song-lyrics-emotion-analyzer
```

### 2️⃣ Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

### Then open the local URL (default: http://localhost:8501).

---

## 🎨 Sample Output

### Input Lyrics:
```bash
I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
```

### Output:
```bash
🎭 Predicted Emotion: LOVE (92.3%)
🧭 Sentiment: Positive 😊
```

---

## 📚 Future Improvements

- 🎵 Fine-tune the model on real song lyric datasets
- 🗣️ Add multilingual lyric support
- 🌐 Deploy on Streamlit Cloud or Hugging Face Spaces

---

## 👨‍💻 Author
Ishan Jain
🎓 B.Tech (AI & ML), Manipal University Jaipur
