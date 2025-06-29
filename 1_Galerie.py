import streamlit as st
import os

st.set_page_config(page_title="Galerie d'amour 💘")

st.title("📸 Nos beaux souvenirs")

photos_dir = "assets/photos"

if not os.path.exists(photos_dir):
    st.warning("Ajoute tes photos dans le dossier `assets/photos/`")
else:
    photos = [f for f in os.listdir(photos_dir) if f.endswith((".jpg", ".png", ".jpeg"))]
    if not photos:
        st.info("Aucune photo trouvée pour l’instant.")
    else:
        for photo in photos:
            st.image(f"{photos_dir}/{photo}", use_column_width=True, caption="Souvenir d’amour 💞")
