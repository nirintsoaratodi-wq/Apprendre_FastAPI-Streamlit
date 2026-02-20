# 📖 Explication du Frontend Streamlit

## 📁 Structure

```
frontend/
└── app.py          ← L'application Streamlit (interface utilisateur)
```

## 🔧 Comment ça marche ?

Le frontend Streamlit communique avec l'API FastAPI via des **requêtes HTTP** :

```
┌─────────────────┐     POST /ml/predict     ┌─────────────────┐
│    Streamlit     │  ──────────────────────► │     FastAPI      │
│   (Port 8501)   │  ◄──────────────────────  │   (Port 8000)   │
│                  │     JSON Réponse         │                  │
└─────────────────┘                           └─────────────────┘
```

**L'utilisateur** remplit un formulaire → **Streamlit** envoie les données à **FastAPI** → **FastAPI** fait la prédiction avec le modèle ML → **Streamlit** affiche le résultat.

---

## 🧩 Les composants Streamlit utilisés

| Composant | Rôle |
|-----------|------|
| `st.set_page_config()` | Configure le titre et l'icône de l'onglet du navigateur |
| `st.title()` | Affiche le titre principal de la page |
| `st.selectbox()` | Menu déroulant pour choisir le genre (Homme/Femme) |
| `st.slider()` | Curseur glissant pour choisir l'âge (18-60 ans) |
| `st.number_input()` | Champ numérique pour entrer le salaire (0-150 000) |
| `st.button()` | Bouton cliquable pour lancer la prédiction |
| `st.success()` | Message vert si la personne va acheter |
| `st.warning()` | Message orange si la personne ne va pas acheter |
| `st.metric()` | Affiche la probabilité d'achat en pourcentage |
| `st.error()` | Message rouge en cas d'erreur |

---

## 📡 La communication avec l'API

Quand l'utilisateur clique sur **"Prédire"** :

1. On crée un dictionnaire `payload` avec les données du formulaire :
```python
payload = {"gender": 0, "age": 30, "estimated_salary": 50000}
```

2. On envoie une requête **POST** à l'API avec `requests.post()` :
```python
response = requests.post("http://127.0.0.1:8000/ml/predict", json=payload)
```

3. L'API retourne une réponse **JSON** :
```json
{"prediction": 0, "probability": 0.1523}
```

4. Streamlit affiche le résultat avec `st.success()` ou `st.warning()`

---

## 🚀 Comment lancer

```bash
# Terminal 1 — Lancer l'API FastAPI (depuis app/)
py main.py

# Terminal 2 — Lancer le Frontend Streamlit (depuis frontend/)
streamlit run app.py
```

L'interface sera accessible sur **http://localhost:8501**
