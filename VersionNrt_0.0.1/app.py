import streamlit as st
import requests

# ---------------------------------------------------------------------------
# Configuration de la page
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="🌸 Prédiction Iris - Nirintsoa",
    page_icon="🌺",
    layout="centered",
)

# ---------------------------------------------------------------------------
# URL de l'API FastAPI (par défaut localhost:8000)
# ---------------------------------------------------------------------------
API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------------------------------
# Mapping des classes Iris
# ---------------------------------------------------------------------------
IRIS_CLASSES = {
    0: {"nom": "Setosa", "emoji": "🌼", "couleur": "#FF6B6B"},
    1: {"nom": "Versicolor", "emoji": "🌸", "couleur": "#4ECDC4"},
    2: {"nom": "Virginica", "emoji": "🌺", "couleur": "#A66CFF"},
}

# ---------------------------------------------------------------------------
# CSS personnalisé pour un design moderne
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    /* ---------- Fond général ---------- */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }

    /* ---------- Titre principal ---------- */
    .main-title {
        text-align: center;
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #A66CFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        color: #b0b0d0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* ---------- Carte résultat ---------- */
    .result-card {
        background: rgba(255,255,255,0.07);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 2rem 2.5rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.12);
        margin-top: 1.5rem;
    }
    .result-emoji { font-size: 4rem; }
    .result-name {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 0.5rem;
    }
    .result-label {
        color: #b0b0d0;
        font-size: 0.95rem;
        margin-top: 0.3rem;
    }

    /* ---------- Info box ---------- */
    .info-box {
        background: rgba(255,255,255,0.05);
        border-left: 4px solid #4ECDC4;
        border-radius: 8px;
        padding: 1rem 1.2rem;
        margin-top: 1.5rem;
        color: #d0d0e8;
        font-size: 0.9rem;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.95);
    }

    /* ---------- Status connexion ---------- */
    .status-ok {
        color: #4ECDC4;
        font-weight: 600;
    }
    .status-ko {
        color: #FF6B6B;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# En-tête
# ---------------------------------------------------------------------------
st.markdown('<p class="main-title">🌸 Prédiction Iris</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">Application de Machine Learning — par Nirintsoa</p>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Vérification de la connexion API
# ---------------------------------------------------------------------------
api_ok = False
try:
    resp = requests.get(f"{API_URL}/", timeout=3)
    if resp.status_code == 200:
        api_ok = True
except Exception:
    pass

if api_ok:
    st.markdown(
        '<p class="status-ok">✅ API connectée (FastAPI)</p>',
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<p class="status-ko">❌ API non disponible — lance d\'abord : '
        '<code>python main.py</code></p>',
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Sidebar — Entrée des paramètres
# ---------------------------------------------------------------------------
st.sidebar.markdown("## 🔬 Paramètres de la fleur")
st.sidebar.markdown("Ajustez les mesures de la fleur Iris :")

sepal_length = st.sidebar.slider("Longueur du sépale (cm)", 4.0, 8.0, 5.8, 0.1)
sepal_width = st.sidebar.slider("Largeur du sépale (cm)", 2.0, 4.5, 3.0, 0.1)
petal_length = st.sidebar.slider("Longueur du pétale (cm)", 1.0, 7.0, 4.0, 0.1)
petal_width = st.sidebar.slider("Largeur du pétale (cm)", 0.1, 2.5, 1.2, 0.1)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Valeurs sélectionnées")
st.sidebar.markdown(f"""
| Mesure | Valeur |
|--------|--------|
| Sépale L | **{sepal_length}** cm |
| Sépale W | **{sepal_width}** cm |
| Pétale L | **{petal_length}** cm |
| Pétale W | **{petal_width}** cm |
""")

# ---------------------------------------------------------------------------
# Bouton de prédiction
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_btn = st.button("🚀 Prédire l'espèce", use_container_width=True)

if predict_btn:
    if not api_ok:
        st.error("⚠️ L'API n'est pas disponible. Lance d'abord le serveur avec `python main.py`")
    else:
        with st.spinner("Envoi des données à l'API..."):
            try:
                params = {
                    "sepal_length": sepal_length,
                    "sepal_width": sepal_width,
                    "petal_length": petal_length,
                    "petal_width": petal_width,
                }
                response = requests.get(f"{API_URL}/predict", params=params, timeout=5)
                result = response.json()

                prediction = result.get("prediction", -1)
                iris_info = IRIS_CLASSES.get(prediction, {
                    "nom": "Inconnu",
                    "emoji": "❓",
                    "couleur": "#888",
                })

                st.markdown(f"""
                <div class="result-card">
                    <div class="result-emoji">{iris_info['emoji']}</div>
                    <div class="result-name" style="color:{iris_info['couleur']}">
                        Iris {iris_info['nom']}
                    </div>
                    <div class="result-label">Classe prédite : {prediction}</div>
                </div>
                """, unsafe_allow_html=True)

                st.success(f"✅ Prédiction réussie : **Iris {iris_info['nom']}**")

            except requests.exceptions.ConnectionError:
                st.error("❌ Impossible de se connecter à l'API. Vérifie que le serveur est lancé.")
            except Exception as e:
                st.error(f"❌ Erreur : {e}")

# ---------------------------------------------------------------------------
# Section d'information
# ---------------------------------------------------------------------------
st.markdown("""
<div class="info-box">
    <strong>💡 Comment utiliser cette application ?</strong><br>
    1. Lance l'API : <code>python main.py</code><br>
    2. Lance ce dashboard : <code>streamlit run app.py</code><br>
    3. Ajuste les paramètres dans la barre latérale<br>
    4. Clique sur <strong>Prédire</strong> pour obtenir le résultat !
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Section espèces Iris
# ---------------------------------------------------------------------------
st.markdown("### 🌿 Les 3 espèces d'Iris")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">🌼</div>
        <div class="result-name" style="color:#FF6B6B; font-size:1.3rem;">Setosa</div>
        <div class="result-label">Classe 0</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">🌸</div>
        <div class="result-name" style="color:#4ECDC4; font-size:1.3rem;">Versicolor</div>
        <div class="result-label">Classe 1</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">🌺</div>
        <div class="result-name" style="color:#A66CFF; font-size:1.3rem;">Virginica</div>
        <div class="result-label">Classe 2</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#666; font-size:0.85rem;">'
    "Projet Nirintsoa — Formation Data Science 2026 — IDEA Academy"
    "</p>",
    unsafe_allow_html=True,
)
