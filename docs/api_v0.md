# API V0 – Spécification minimale

## Endpoint
- **Route** : `/predict`
- **Méthode** : POST

## Input attendu
```json
{
  "text": "I love this project!"
}
```
## output attendu
```json
{
  "sentiment": "positive"
}
```
Notes

Implémenté avec FastAPI.

Testé en local via Postman.

Modèle utilisé : Logistic Regression (baseline).