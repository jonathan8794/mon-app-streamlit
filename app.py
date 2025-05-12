import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ma première vraie app Streamlit")
st.write("Bienvenue sur cette app interactive ! 😊")

# Image
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Streamlit_logo_vertical_primary.png/480px-Streamlit_logo_vertical_primary.png",
    width=200,
    caption="Logo officiel Streamlit"
)

# 📊 Données
data = pd.DataFrame({
    "Mois": ["Jan", "Fév", "Mars", "Avr", "Mai"],
    "Ventes": [100, 120, 90, 130, 150]
})

# 🔘 Sélecteur
mois_choisi = st.selectbox("Choisissez un mois :", data["Mois"])
vente = data[data["Mois"] == mois_choisi]["Ventes"].values[0]
st.write(f"🔎 En {mois_choisi}, les ventes étaient de **{vente} unités**.")

# 📈 Graphique
st.subheader("Évolution des ventes 📈")
fig, ax = plt.subplots()
ax.plot(data["Mois"], data["Ventes"], marker='o', color='blue')
ax.set_xlabel("Mois")
ax.set_ylabel("Ventes")
ax.set_title("Ventes par mois")
st.pyplot(fig)


