# 🌸 Iris Classifier — Nirintsoa 0.0.1

> Application de classification des fleurs Iris utilisant le Machine Learning, une API FastAPI et une interface Streamlit moderne.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20développement-yellow)

---

## 📋 Table des matières

- [Description](#-description)
- [Fonctionnalités](#-fonctionnalités)
- [Architecture du projet](#-architecture-du-projet)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Aperçu de l'API](#-aperçu-de-lapi)
- [Technologies utilisées](#-technologies-utilisées)
- [Auteur](#-auteur)

---

## 📖 Description

**Iris Classifier** est un projet de Data Science qui prédit l'espèce d'une fleur Iris (Setosa, Versicolor ou Virginica) en fonction de 4 mesures :

| Mesure | Description |
|--------|-------------|
| Longueur du sépale | en cm |
| Largeur du sépale | en cm |
| Longueur du pétale | en cm |
| Largeur du pétale | en cm |

Le projet combine un **modèle de Machine Learning** pré-entraîné avec une **API REST** (FastAPI) et une **interface utilisateur web** élégante (Streamlit).

---

## ✨ Fonctionnalités

- 🤖 **Prédiction en temps réel** — Classification instantanée via un modèle ML
- 🎨 **Interface moderne** — Design sombre avec dégradés et animations
- 🔌 **API REST** — Endpoint `/predict` pour intégration externe
- 📊 **Notebook d'analyse** — Exploration et entraînement du modèle documentés
- ⚡ **Vérification de connexion** — Détection automatique du statut de l'API

---

## 🏗 Architecture du projet

```
Nirintsoa0.0.1/
├── main.py              # 🚀 Serveur FastAPI (backend API)
├── app.py               # 🎨 Interface Streamlit (frontend)
├── front.py             # 📄 Script frontend alternatif
├── model.joblib         # 🤖 Modèle ML pré-entraîné
├── scaler.joblib        # 📏 Scaler pour normalisation des données
├── notebook.ipynb       # 📓 Notebook Jupyter (analyse & entraînement)
├── insurance.xlsx       # 📊 Jeu de données
├── requirements.txt     # 📦 Dépendances Python
└── README.md            # 📖 Ce fichier
```

---

## 🔧 Prérequis

- **Python** 3.10 ou supérieur
- **pip** (gestionnaire de paquets Python)

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ONG-IDEA-Academy/Formation-DS-2026.git
cd Formation-DS-2026/Nirintsoa0.0.1
```

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

### Étape 1 — Lancer le serveur API

```bash
python main.py
```

Le serveur FastAPI démarre sur `http://127.0.0.1:8000`.

### Étape 2 — Lancer l'interface Streamlit

Dans un **second terminal** :

```bash
streamlit run app.py
```

L'interface s'ouvre automatiquement dans votre navigateur sur `http://localhost:8501`.

### Étape 3 — Faire une prédiction

1. Ajustez les **sliders** dans la barre latérale (mesures de la fleur)
2. Cliquez sur **🚀 Prédire l'espèce**
3. Le résultat s'affiche avec l'espèce prédite et un émoji correspondant

---

## 🔌 Aperçu de l'API

### `GET /`

Page d'accueil de l'API.

```json
{ "message": "Bienvenue dans mon API" }
```

### `GET /predict`

Prédiction de l'espèce d'Iris.

**Paramètres :**

| Paramètre | Type | Description |
|-----------|------|-------------|
| `sepal_length` | `float` | Longueur du sépale (cm) |
| `sepal_width` | `float` | Largeur du sépale (cm) |
| `petal_length` | `float` | Longueur du pétale (cm) |
| `petal_width` | `float` | Largeur du pétale (cm) |

**Exemple :**

```
GET /predict?sepal_length=5.8&sepal_width=3.0&petal_length=4.0&petal_width=1.2
```

**Réponse :**

```json
{ "prediction": 1 }
```

| Code | Espèce |
|------|--------|
| 0 | 🌼 Setosa |
| 1 | 🌸 Versicolor |
| 2 | 🌺 Virginica |

---

## 🛠 Technologies utilisées

| Technologie | Rôle |
|-------------|------|
| **Python** | Langage principal |
| **FastAPI** | API REST backend |
| **Uvicorn** | Serveur ASGI |
| **Streamlit** | Interface utilisateur web |
| **Scikit-learn** | Entraînement du modèle ML |
| **Joblib** | Sérialisation du modèle |
| **Pandas / NumPy** | Manipulation des données |
| **Pydantic** | Validation des données |

---

## 👤 Auteur

**Nirintsoa** — *Formation Data Science 2026* — [IDEA Academy](https://idea-academy.mg)

---

## 📝 Licence

Ce projet est réalisé dans le cadre de la **Formation Data Science 2026** à IDEA Academy.

---

<p align="center">
  <i>Fait avec ❤️ par Nirintsoa — 2026</i>
</p>
