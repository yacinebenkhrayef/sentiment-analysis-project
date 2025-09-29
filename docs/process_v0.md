# Processus V0 – Pipeline du projet

## 🔹 Étapes du pipeline (V0)
1. **Dataset**
   - Source : Sentiment140 (Kaggle)
   - Échantillon utilisé : 2 000 tweets
   - Stockage : local (CSV + MongoDB/PostgreSQL en test)

2. **Prétraitement NLP**
   - Nettoyage : suppression des URLs, mentions, hashtags, emojis
   - Tokenisation : NLTK
   - Split dataset : 70% train / 15% validation / 15% test

3. **Modèle baseline**
   - Méthode : TF-IDF + Logistic Regression
   - Librairie : scikit-learn
   - Évaluation : Accuracy, F1-score

4. **API minimale**
   - Backend : FastAPI
   - Endpoint `/predict`
   - Input : texte brut
   - Output : sentiment (positif, négatif, neutre)

## 🔹 Outils utilisés (V0)
- **Python** : 3.11
- **Librairies Data** : pandas, numpy, matplotlib, seaborn
- **Librairies NLP** : NLTK, regex
- **Modélisation** : scikit-learn
- **Backend** : FastAPI, uvicorn
- **Frontend minimal** : React + Material-UI (page test)
