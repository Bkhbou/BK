import streamlit as st
import os

st.set_page_config(page_title=" Khady❤️", page_icon="💖", layout="centered")

# --- Menu latéral ---
menu = st.sidebar.radio("Navigation", ["🏠 Accueil", "📸 Galerie", "💌 Lettre d'amour"])

# --- Page d'accueil ---
if menu == "🏠 Accueil":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #ff4b6e;"> 7ayatii 💕</h1>
            <p style="font-size: 20px;">Ce site a été créé juste pour toi, pour te montrer combien je t’aime. 💌</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image("assets/1.jpg", width=300, caption="💖 Lbidaye 💖")

# --- Galerie de photos ---
elif menu == "📸 Galerie":
    st.title("📸 Nos beaux souvenirs")
    photos_dir = "assets/photos"
    if not os.path.exists(photos_dir):
        st.warning("Ajoute les photos 2, 3, 4 dans le dossier `assets/photos/`")
    else:
        photos = ["2.JPG"]
        for photo in photos:
            path = os.path.join(photos_dir, photo)
            if os.path.exists(path):
                st.image(path, use_column_width=True, caption=f"Souvenir {photo.split('.')[0]} 💞")
            else:
                st.warning(f"{photo} est manquante dans `assets/photos/`")

# --- Lettre d'amour ---
elif menu == "💌 Lettre d'amour":
    st.title("💌 Ma lettre pour toi")
    st.markdown("""
    <p style='font-size:18px;'>
    Ma chérie,<br><br>
    Ce petit site est ma façon à moi de te dire combien tu es importante pour moi...<br><br>
    Je t’aime plus que tout 💖<br><br>
    (Tu peux écrire ta vraie lettre ici plus tard)
    </p>
    """, unsafe_allow_html=True)
