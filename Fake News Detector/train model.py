import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(BASE_DIR, "data", "news dataset.csv")
models_dir = os.path.join(BASE_DIR, "models")
reports_dir = os.path.join(BASE_DIR, "reports")

os.makedirs(models_dir, exist_ok=True)
os.makedirs(reports_dir, exist_ok=True)

df = pd.read_csv(data_path)

X = df["title"]
y = df["label"]

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

joblib.dump(model, os.path.join(models_dir, "fake news model.pkl"))
joblib.dump(vectorizer, os.path.join(models_dir, "tfidf vectorizer.pkl"))

report_path = os.path.join(reports_dir, "evaluation report.txt")
with open(report_path, "w") as f:
    f.write("FAKE NEWS DETECTOR REPORT\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Accuracy : {accuracy:.4f}\n")
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall   : {recall:.4f}\n")
    f.write(f"F1 Score : {f1:.4f}\n\n")
    f.write(report)

print("Training Complete")
print("Model Saved")
print("Vectorizer Saved")
print("Report Generated")