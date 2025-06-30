import streamlit as st
import os

# --- Configuration de la page ---
st.set_page_config(page_title="Khady ❤️", page_icon="💖", layout="centered")

# --- Sécurité : code d'accès ---
st.markdown("<h2 style='text-align: center;'>🔐 Dir Code</h2>", unsafe_allow_html=True)
code = st.text_input("Gtlak Dir Codak :", type="password")

if code != "2007":
    st.warning("🛑 4ik mahi Khady. Mreg gtlak...")
    st.stop()

# --- Menu latéral ---
menu = st.sidebar.radio("Navigation", ["🏠 Accueil", "📸 Galerie", "💌 ....."])

# --- Page Accueil ---
if menu == "🏠 Accueil":
    st.markdown(
        """
        <div style="text-align: center;">
            <h1 style="color: #ff4b6e;">7ayatii 💕</h1>
            <p style="font-size: 20px;">
                4i page mu3dle 3n sta7fii , leyle sa7feytinii nin 58ti. 💌
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image("assets/1.jpg", width=300, caption="💖 Lbidaye 💖")

# --- Galerie de photos ---
elif menu == "📸 Galerie":
    st.title("📸 Suwarne")

    photos_dir = "assets"
    photos = ["2.JPG", "3.jpg", "4.JPG", "5.JPG"]

    if not os.path.exists(photos_dir):
        st.warning("Le dossier 'assets' est introuvable.")
    else:
        for photo in photos:
            path = os.path.join(photos_dir, photo)
            if os.path.exists(path):
                st.image(path, use_container_width=True, caption=f"Khdeydy {photo.split('.')[0]} 💞")
            else:
                st.error(f"❌ {photo} est manquante dans le dossier 'assets'")

# --- Message d'amour ---
elif menu == "💌 .....":
    st.title("💌 Shi ma yged yngal kun l Hayatii ane")
    st.markdown("""
    <p style='font-size:18px;'>
    7abibty,<br><br>
    KHadijtii hayatii shlahi nktb ga33 w9ed 3liye 4e lknt lahi ngull ...<br><br>
    Love U 7atte B3d 💖<br><br>
    </p>
    """, unsafe_allow_html=True)
