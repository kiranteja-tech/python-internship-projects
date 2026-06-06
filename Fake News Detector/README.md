# Fake News Detector

## Project Overview

Fake News Detector is a Machine Learning and Natural Language Processing (NLP) project that classifies news headlines as either Real News or Fake News.

The system processes news headlines using TF-IDF vectorization and applies a Logistic Regression classification model to determine the authenticity of the news. The application provides single headline prediction, confidence scores, and batch prediction through CSV file uploads.

This project demonstrates practical applications of Machine Learning, Text Classification, and Natural Language Processing using Python.

---

## Features

* News headline classification
* Fake News detection
* Real News detection
* Text preprocessing
* TF-IDF vectorization
* Logistic Regression model training
* Model evaluation and testing
* Confidence score prediction
* Batch CSV upload for multiple predictions
* Downloadable prediction results
* Streamlit web application interface

---

## Technologies Used

| Technology | Purpose |
| --- | --- |
| **Python** | Programming Language |
| **Pandas** | Data Processing |
| **Scikit-Learn** | Machine Learning |
| **TF-IDF Vectorizer** | Text Feature Extraction |
| **Logistic Regression** | Classification Model |
| **Joblib** | Model Serialization |
| **Streamlit** | Web Application Interface |

---

## Project Structure

```text
Fake News Detector/
│
├── data/
│   └── news dataset.csv
│
├── models/
│   ├── fake news model.pkl
│   └── tfidf vectorizer.pkl
│
├── reports/
│   └── evaluation report.txt
│
├── train model.py
├── app.py
├── requirements.txt
└── README.md

```

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt

```

Or install manually:

```bash
pip install pandas scikit-learn streamlit joblib numpy

```

---

## Dataset

The project uses a CSV dataset containing news headlines and labels.

**Example:**

```csv
title,label
Government announces new agricultural support program,1
Scientists discover a new species in the Amazon rainforest,1
Aliens officially elected as world leaders,0
Moon made entirely of cheese confirms study,0

```

### Labels

* **1:** Real News
* **0:** Fake News

---

## Machine Learning Workflow

```text
Dataset ➔ Data Cleaning ➔ TF-IDF Vectorization ➔ Train-Test Split ➔ Model Training ➔ Model Evaluation ➔ Model Saving ➔ Streamlit Deployment

```

---

## Model Training

Run the training script:

```bash
python "train model.py"

```

The script performs:

* Dataset loading
* Feature extraction using TF-IDF
* Train-test split
* Logistic Regression training
* Model evaluation
* Model saving
* Evaluation report generation

### Generated Files

After training, the following files are generated automatically inside the project folder:

```text
models/
├── fake news model.pkl
└── tfidf vectorizer.pkl

reports/
└── evaluation report.txt

```

### Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Classification Report

**Example Output:**

```text
Accuracy : 0.92
Precision: 0.91
Recall   : 0.93
F1 Score : 0.92

```

---

## Running the Application

Start the Streamlit application from your terminal:

```bash
streamlit run app.py

```

The application opens automatically in your browser at:
`http://localhost:8501`

### Single Headline Prediction

* **Input:** *Scientists discover new exoplanet*
* **Output:** * **Prediction:** Real News
* **Confidence:** 94.5%



### Batch CSV Prediction

Upload a CSV file containing a column named `title`:

| title |
| --- |
| Government launches new employment scheme |
| Aliens elected as world leaders |
| Scientists publish climate study |
| Moon made of cheese confirmed |

**Output Table displayed in Web App:**

| Title | Prediction |
| --- | --- |
| Government launches new employment scheme | Real News |
| Aliens elected as world leaders | Fake News |
| Scientists publish climate study | Real News |
| Moon made of cheese confirmed | Fake News |

> **Note:** Users can download these processed prediction results directly as a new CSV file.

---

## Deliverables

The project maintains and generates:

* **Dataset:** `data/news dataset.csv`
* **Trained Model:** `models/fake news model.pkl`
* **TF-IDF Vectorizer:** `models/tfidf vectorizer.pkl`
* **Evaluation Report:** `reports/evaluation report.txt`
* **Streamlit Application:** `app.py`

---

## Learning Outcomes

This project demonstrates:

* Natural Language Processing (NLP)
* Text Classification
* Feature Engineering
* TF-IDF Vectorization
* Machine Learning Model Training
* Model Evaluation
* Streamlit Application Development
* Batch Prediction Systems

---

## Future Enhancements

* Deep Learning Models (LSTM, BERT)
* Full News Article Classification
* Live News API Integration
* Sentiment Analysis Integration
* Multilingual News Detection
* Dashboard Analytics
* Database Integration

---

## Author

Academic project developed to demonstrate Machine Learning, Natural Language Processing, and Fake News Detection using Python.

## License

This project is intended for educational, learning, and portfolio purposes.