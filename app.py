import streamlit as st
import os

st.set_page_config(page_title="Pour Toi ❤️", page_icon="💖", layout="centered")

# --- Barre de navigation ---
menu = st.sidebar.radio("Navigation", ["🏠 Accueil", "📸 Galerie", "💌 Lettre d'amour"])

# --- Accueil ---
if menu == "🏠 Accueil":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #ff4b6e;">Bienvenue mon amour 💕</h1>
            <p style="font-size: 20px;">Ce site a été créé juste pour toi, pour te montrer combien je t’aime. 💌</p>
            <img src="https://i.imgur.com/Z5cU3uG.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Galerie de photos ---
elif menu == "📸 Galerie":
    st.title("📸 Nos beaux souvenirs")
    photos_dir = "assets/photos"
    if not os.path.exists(photos_dir):
        st.warning("Ajoute tes photos dans le dossier `assets/photos/`")
    else:
        photos = [f for f in os.listdir(photos_dir) if f.endswith((".jpg", ".png", ".jpeg"))]
        if not photos:
            st.info("Aucune photo pour l’instant.")
        else:
            for photo in photos:
                st.image(f"{photos_dir}/{photo}", use_column_width=True, caption="Souvenir d’amour 💞")

# --- Lettre d'amour ---
elif menu == "💌 Lettre d'amour":
    st.title("💌 Ma lettre pour toi")
    st.markdown("""
    <p style='font-size:18px;'>
    Ma chérie,<br><br>
    Ce petit site est ma façon à moi de te dire combien tu es importante pour moi...<br><br>
    (Signe ici ta vraie lettre d’amour 😍)
    </p>
    """, unsafe_allow_html=True)
