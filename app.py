import streamlit as st
import os
from datetime import datetime

# --- Configuration de la page ---
st.set_page_config(page_title="Khady ❤️", page_icon="💖", layout="centered")

# --- Mots de passe ---
USER_PASSWORD = "02012025"   # Mot de passe utilisateur
ADMIN_PASSWORD = "admin2025" # Mot de passe admin pour voir la dernière connexion
LAST_LOGIN_FILE = "last_login.txt"

# --- Sécurité : gestion de session ---
if "authentifie" not in st.session_state:
    st.session_state.authentifie = False
if "admin" not in st.session_state:
    st.session_state.admin = False

# --- Fonction pour lire la dernière connexion ---
def lire_derniere_connexion():
    if os.path.exists(LAST_LOGIN_FILE):=bankily:"+222 31720304"
        with open(LAST_LOGIN_FILE, "r") as f:
            return f.read().strip()
    return "Aucune connexion précédente."

# --- Fonction pour sauvegarder la date actuelle comme dernière connexion ---
def sauvegarder_connexion():
    now = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    with open(LAST_LOGIN_FILE, "w") as f:
        f.write(now)
    return now

# --- Authentification ---
if not st.session_state.authentifie:
    st.markdown("<h2 style='text-align: center;'>🔐 Password</h2>", unsafe_allow_html=True)
    code = st.text_input("Gtlak Dir Codak :", type="password")
    if code == USER_PASSWORD:
        st.session_state.authentifie = True
        sauvegarder_connexion()
        st.rerun()
    elif code == ADMIN_PASSWORD:
        st.session_state.authentifie = True
        st.session_state.admin = True
        st.rerun()
    elif code != "":
        st.error("⛔ Mreg Gtlak 4e ma y3nik")

# --- Contenu après authentification ---
if st.session_state.authentifie:
    st.success("Welcome Hayatiii ❤️ !")

    # --- Affichage dernière connexion uniquement pour l'admin ---
    if st.session_state.admin:
        derniere_connexion = lire_derniere_connexion()
        st.warning(f"🔒 [ADMIN] Dernière connexion : {derniere_connexion}")

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
        st.image("assets/1.jpg", width=300, caption="💖Ezyen message ga6a jani 💖")

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
                    st.image(path, use_container_width=True, caption="Khdeydy 7abibtyy 💞")
                else:
                    st.error(f"❌ {photo} est manquante dans le dossier 'assets'")

    # --- Message d'amour ---
    elif menu == "💌 .....":
        st.title("💌 Shi ma yged yngal kun l Hayatii ane")
        st.markdown("""
        <p style='font-size:18px;'>
        7abibty,<br><br>
        Khady hayatii tellement nb9iiik , ezyen 7ad ga6 jbart w mzlt lahi njbr ,
        mani gayl en vm 7ad esfee mnk niye , ma kivkk nass nb9iik , ...<br><br>
        Love UUUU Today , Tomorrow and Forever 💖<br><br>
        Bechir hayateek <br><br>
        </p>
        """, unsafe_allow_html=True)
