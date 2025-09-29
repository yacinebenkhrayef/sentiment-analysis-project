# 📊 Projet – Analyse des Sentiments et Détection de Tendances sur les Réseaux Sociaux

## 🎯 Objectif du projet
Développer une application **end-to-end** capable de :
- Classifier automatiquement les sentiments (positif, négatif, neutre) dans des posts issus de réseaux sociaux.
- Détecter les tendances émergentes (hashtags, sujets, mots-clés).
- Visualiser les résultats dans une **interface web interactive**.

Projet réalisé par **4 étudiants en Data Science** dans le cadre d’un projet académique, sous la supervision de l’encadrant.  
Méthodologie adoptée : **versions incrémentales (V0 → V4)** avec alternance des rôles et un **chef de projet permanent**.

---

## 🚀 Roadmap des Versions
| Version | Description | Dataset | Modèle | API | Frontend |
|---------|-------------|---------|--------|-----|----------|
| **V0 (Sem. 1–2)** | Prototype minimal | Sentiment140 (2k tweets) | TF-IDF + Logistic Regression | FastAPI `/predict` | React (page test) |
| **V1 (Sem. 3–4)** | Première version complète | 50k tweets | DistilBERT fine-tuné | API `/predict` + `/trends` | Dashboard simple |
| **V2 (Sem. 5–7)** | Amélioration des modèles et visualisations | 200k tweets | DistilBERT optimisé + LDA | API enrichie | Dashboard avancé (graphiques + wordclouds) |
| **V3 (Sem. 8–10)** | Passage à l’échelle | 1.6M tweets + API live (Twitter/Reddit) | BERT + BERTopic | Backend optimisé | Dashboard interactif |
| **V4 (Sem. 11–12)** | Version finale déployée | Flux temps réel | BERT optimisé | API déployée (Docker/Heroku) | Dashboard complet + démo |

---

## 🛠️ Technologies utilisées
### Data & NLP
- **pandas, numpy, matplotlib, seaborn** → analyse et visualisation
- **NLTK, SpaCy** → nettoyage, tokenisation, lemmatisation
- **HuggingFace Transformers** → modèles BERT/DistilBERT
- **scikit-learn** → baseline (TF-IDF, Logistic Regression)

### Backend
- **FastAPI** → API REST rapide et légère
- **uvicorn** → serveur ASGI
- **MongoDB/PostgreSQL** → stockage

### Frontend
- **React (Vite)** → interface utilisateur
- **Material-UI / Tailwind** → design
- **Recharts, WordCloud** → visualisations

### Déploiement
- **Docker** → conteneurisation
- **Heroku / Render** → backend
- **Vercel / Netlify** → frontend

---

## 👥 Organisation de l’équipe
- **Étudiant 1 (CP)** : Chef de projet permanent, coordination, gestion Jira/Trello, doc.
- **Étudiants 1–4** : Tous participent aux phases (Data, NLP, DL, Frontend, Backend) en **rotation des rôles**.
- Alternance prévue toutes les 2 semaines.

---

## 📂 Structure du dépôt
.
├── docs/ # Documentation détaillée
│ ├── dataset_v0.md
│ ├── process_v0.md
│ ├── api_v0.md
│ └── DoD_v0.md
├── backend/ # Code FastAPI
├── frontend/ # Code React
├── notebooks/ # Jupyter notebooks pour exploration et modèles
├── data/ # Datasets utilisés (ou lien vers Kaggle)
└── README.md # Documentation principale

---

## 📌 Sprint 1 – V0
### Objectifs
- Mise en place des environnements (Python, FastAPI, React).
- Collecte et exploration d’un dataset initial (2k tweets).
- Prétraitement minimal NLP.
- Baseline ML (TF-IDF + Logistic Regression).
- API `/predict` minimale.

### Livrables
- Dataset brut + nettoyé.
- Modèle baseline entraîné et sauvegardé.
- API fonctionnelle en local.
- Documentation initiale.
- Suivi Jira/Trello à jour.

---

## 📈 Suivi projet
- **Gestion de projet** : Jira (sprints, backlog, user stories).
- **Versioning** : GitHub (branches par feature, commits explicites).
- **Livrables** : Documentation dans `/docs`, code organisé en backend/frontend.

---

## 📜 Licence
Projet académique – non commercial.


## 🚀 Instructions pour cloner et lancer
```bash
git clone https://github.com/yacinebenkhrayef/sentiment-analysis-project.git
cd sentiment-analysis-project
