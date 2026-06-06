import os
import streamlit as st
import pandas as pd
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "models", "fake news model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "tfidf vectorizer.pkl")

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

st.title("Fake News Detector")

st.header("Single Headline Prediction")

headline = st.text_input("Enter News Headline")

if st.button("Predict"):
    vector = vectorizer.transform([headline])
    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector).max() * 100

    if prediction == 1:
        result = "Real News"
    else:
        result = "Fake News"

    st.success(f"Prediction: {result}")
    st.write(f"Confidence: {confidence:.2f}%")

st.divider()

st.header("Batch CSV Upload")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    batch_df = pd.read_csv(uploaded_file)
    vectors = vectorizer.transform(batch_df["title"])
    predictions = model.predict(vectors)

    batch_df["Prediction"] = [
        "Real News" if p == 1 else "Fake News" for p in predictions
    ]

    st.dataframe(batch_df)

    csv = batch_df.to_csv(index=False)

    st.download_button("Download Results", csv, "predictions.csv", "text/csv")