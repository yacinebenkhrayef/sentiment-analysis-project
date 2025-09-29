# Dataset V0 – Sentiment Analysis

## 📌 Source
- **Nom** : Sentiment140 Dataset  
- **Lien** : [https://www.kaggle.com/datasets/kazanova/sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)  
- **Format** : CSV (~1.6 million de tweets)  

## 📊 Taille utilisée pour V0
- Pour le **prototype initial (V0)**, nous utilisons **2 000 tweets échantillonnés**.  
- Cela permet :
  - d’accélérer l’entraînement du baseline,
  - d’éviter les temps longs d’exécution,
  - de valider rapidement la faisabilité du projet.

## 🌍 Langue
- Anglais (tweets majoritairement en anglais).
- Avantage : simplicité pour un premier prototype (outils NLP bien adaptés).

## ⚠️ Problèmes connus
- Données bruyantes :  
  - doublons,  
  - tweets vides ou très courts,  
  - emojis, hashtags, URLs, mentions (@user),  
  - mélange de langues dans certains cas.  
- Ces problèmes seront traités progressivement dans les étapes de prétraitement NLP.

## ✅ Justification du choix
- **Ouvert et libre** : dataset disponible publiquement sur Kaggle.  
- **Réputation** : largement utilisé dans la recherche en sentiment analysis.  
- **Volume suffisant** : 1,6M tweets si besoin pour passer à l’échelle (versions futures).  
- **Baseline rapide** : possibilité d’utiliser un petit échantillon (2k) pour démarrer rapidement.  

## 🚀 Perspectives (Versions futures)
- V1 : augmenter à 50k tweets pour un modèle plus robuste.  
- V2+ : utiliser le dataset complet (1.6M) + collecte en temps réel (API Twitter/Reddit).  
