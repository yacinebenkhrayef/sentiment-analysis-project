# train_baseline.py (exemple minimal)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Exemple: tu dois remplacer par ton CSV réel. Ici on crée un petit jeu factice.
data = pd.DataFrame({
    "text": ["I love this", "I hate this", "It is okay", "I am happy", "This is bad"],
    "label": ["positif","negatif","neutre","positif","negatif"]
})

X = data["text"]
y = data["label"]
tfidf = TfidfVectorizer()
X_t = tfidf.fit_transform(X)
model = LogisticRegression(max_iter=1000)
model.fit(X_t, y)

os.makedirs("models", exist_ok=True)
joblib.dump({"tfidf": tfidf, "model": model}, "models/baseline.joblib")
print("Saved models/baseline.joblib")
