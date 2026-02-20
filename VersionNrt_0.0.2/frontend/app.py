# ============================================================
# Frontend Streamlit — Interface utilisateur pour l'API de Prédiction
# Ce fichier crée une application web interactive qui envoie
# les données saisies par l'utilisateur à l'API FastAPI
# et affiche le résultat de la prédiction.
# ============================================================

# Importation de streamlit : le framework pour créer des interfaces web facilement
import streamlit as st

# Importation de requests : la bibliothèque pour envoyer des requêtes HTTP à notre API
import requests

# --- CONFIGURATION DE LA PAGE ---
# st.set_page_config() configure les paramètres de la page du navigateur
# Doit être appelé en PREMIER avant tout autre appel Streamlit
st.set_page_config(
    page_title="Prédiction d'Achat",  # Titre de l'onglet du navigateur
    page_icon="🛒",                    # Icône affichée dans l'onglet du navigateur
    layout="centered"                  # Disposition centrée de la page (pas en pleine largeur)
)

# --- URL DE L'API ---
# L'adresse de notre API FastAPI qui tourne en local sur le port 8000
# /ml/predict est l'endpoint POST défini dans route.py
API_URL = "http://127.0.0.1:8000/ml/predict"

# --- TITRE DE L'APPLICATION ---
# st.title() affiche un grand titre en haut de la page
st.title("🛒 Prédiction d'Achat")

# st.write() affiche du texte dans l'application
st.write("Entrez les informations d'un utilisateur pour prédire s'il va acheter le produit.")

# st.markdown("---") crée une ligne horizontale de séparation visuelle
st.markdown("---")

# --- FORMULAIRE DE SAISIE ---
# st.subheader() affiche un sous-titre plus petit que le titre principal
st.subheader("📋 Informations de l'utilisateur")

# st.selectbox() crée un menu déroulant avec des options à choisir
# L'utilisateur choisit "Homme" ou "Femme" et on stocke le choix dans la variable gender_label
gender_label = st.selectbox(
    "Genre :",                         # Le texte affiché au-dessus du menu déroulant
    options=["Homme", "Femme"],        # Les deux options disponibles dans le menu
    index=0                            # index=0 signifie que "Homme" est sélectionné par défaut
)

# Conversion du choix textuel en valeur numérique pour l'API
# Le modèle ML attend 0 pour Male (Homme) et 1 pour Female (Femme)
# C'est le même encodage que celui fait dans le notebook avec data.replace({'Male': 0, 'Female': 1})
gender = 0 if gender_label == "Homme" else 1

# st.slider() crée un curseur glissant pour choisir une valeur numérique
# L'utilisateur peut faire glisser le curseur pour choisir l'âge
age = st.slider(
    "Âge :",                           # Le texte affiché au-dessus du slider
    min_value=18,                      # Valeur minimale du slider (18 ans)
    max_value=60,                      # Valeur maximale du slider (60 ans, comme dans le dataset)
    value=30                           # Valeur par défaut affichée au démarrage (30 ans)
)

# st.number_input() crée un champ de saisie numérique avec des boutons +/-
# L'utilisateur entre le salaire estimé de la personne
estimated_salary = st.number_input(
    "Salaire estimé (€) :",            # Le texte affiché au-dessus du champ
    min_value=0,                       # Valeur minimale autorisée (0 €)
    max_value=150000,                  # Valeur maximale autorisée (150 000 €, comme dans le dataset)
    value=50000,                       # Valeur par défaut affichée au démarrage (50 000 €)
    step=1000                          # Le pas d'incrémentation quand on clique sur +/- (1000 €)
)

# st.markdown("---") crée une autre ligne de séparation
st.markdown("---")

# --- BOUTON DE PRÉDICTION ---
# st.button() crée un bouton cliquable
# Il retourne True quand l'utilisateur clique dessus, False sinon
# use_container_width=True fait que le bouton prend toute la largeur disponible
if st.button("🔮 Prédire", use_container_width=True):

    # --- PRÉPARATION DES DONNÉES ---
    # On crée un dictionnaire Python avec les données saisies par l'utilisateur
    # Les clés ("gender", "age", "estimated_salary") doivent correspondre exactement
    # aux champs du schéma InputData défini dans schema.py
    payload = {
        "gender": gender,                       # 0 (Homme) ou 1 (Femme)
        "age": age,                             # L'âge choisi avec le slider
        "estimated_salary": estimated_salary    # Le salaire entré dans le champ numérique
    }

    # --- ENVOI DE LA REQUÊTE À L'API ---
    # On utilise try/except pour gérer les erreurs possibles (API éteinte, réseau, etc.)
    try:
        # requests.post() envoie une requête HTTP POST à l'URL de notre API
        # json=payload convertit automatiquement le dictionnaire Python en JSON
        # C'est exactement comme si on envoyait depuis Swagger UI ou Postman
        response = requests.post(API_URL, json=payload)

        # --- TRAITEMENT DE LA RÉPONSE ---
        # response.status_code contient le code HTTP retourné par l'API
        # 200 signifie que la requête a réussi (OK)
        if response.status_code == 200:

            # response.json() convertit la réponse JSON en dictionnaire Python
            # Le dictionnaire contient "prediction" et "probability" (définis dans PredictionResponse)
            result = response.json()

            # On extrait la prédiction (0 ou 1) du dictionnaire de réponse
            prediction = result["prediction"]

            # On extrait la probabilité (entre 0.0 et 1.0) du dictionnaire de réponse
            probability = result["probability"]

            # --- AFFICHAGE DU RÉSULTAT ---
            st.markdown("---")

            # st.subheader() affiche un sous-titre pour la section résultats
            st.subheader("📊 Résultat de la prédiction")

            # On affiche un message différent selon la prédiction du modèle
            if prediction == 1:
                # st.success() affiche un message en vert (succès/positif)
                # Le modèle prédit que la personne VA acheter le produit
                st.success(f"✅ Cette personne VA probablement acheter le produit !")
            else:
                # st.warning() affiche un message en orange (avertissement)
                # Le modèle prédit que la personne NE VA PAS acheter le produit
                st.warning(f"❌ Cette personne NE VA probablement PAS acheter le produit.")

            # st.metric() affiche une métrique avec un label et une valeur
            # On affiche la probabilité d'achat en pourcentage (ex: 87.50%)
            # f"{probability * 100:.2f}%" multiplie par 100 et formate avec 2 décimales
            st.metric(
                label="Probabilité d'achat",          # Le label affiché au-dessus de la valeur
                value=f"{probability * 100:.2f} %"     # La valeur formatée en pourcentage
            )

        else:
            # Si le code HTTP n'est pas 200, il y a eu une erreur côté API
            # st.error() affiche un message en rouge (erreur)
            st.error(f"❌ Erreur API — Code : {response.status_code}")

    # except requests.exceptions.ConnectionError gère le cas où l'API n'est pas accessible
    # Cela arrive si le serveur FastAPI n'est pas lancé ou si l'URL est incorrecte
    except requests.exceptions.ConnectionError:
        # On affiche un message d'erreur clair pour aider l'utilisateur à résoudre le problème
        st.error("🚫 Impossible de se connecter à l'API. Vérifiez que le serveur FastAPI est lancé !")
