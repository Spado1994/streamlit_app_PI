import streamlit as st
import datetime
import locale

# Changer la langue pour datetime
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# Ouvrir le fichier des décimales de PI
with open("pi_million.txt", "r") as f:
    d = f.read()

# Nettoyer et ne garder que les décimales
digits_pi = ''.join(filter(str.isdigit, d))
decimales = digits_pi[1:]

st.title("Recherche de date de naissance dans Pi")

# Entrée date de naissance et formattage
date_naissance = st.date_input(
    "Entrez une date de naissance :", 
    format="DD/MM/YYYY", 
    min_value=datetime.date(1925, 1, 1)
    )

# Transformer en string
date_str = str(date_naissance.strftime("%d%m%Y"))

# Effectuer la recherche sans les décimales de PI
if st.button("Chercher la date de naissance"):
    if date_str:
        position = decimales.find(date_str)
        if position != -1:
            st.success(f"La date de naissance est à la position {position} des décimales de PI.")
        else:
            st.error("La date de naissance n'existe pas dans le premier million de décimales.")

# Trouver le jour à partir de la date
jour_semaine = date_naissance.strftime("%A")
st.text(f"Le jour de naissance est le {jour_semaine}")

# Somme des 20 premières décimales
somme_20 = sum(int(decimal) for decimal in decimales[:20])
st.text(f"Somme des 20 premières décimales de π : {somme_20}")

# Somme des 144 premières décimales
somme_144 = sum(int(chiffre) for chiffre in decimales[:144])
st.text(f"Somme des 122 premières décimales de π : {somme_144}")

# Sommes des 1728 premières décimales 
somme_1728 = sum(int(chiffre) for chiffre in decimales[:1728])
st.text(f"Somme des 1778 premières décimales de π : {somme_1728}")

st.subheader("Vidéo : L'incroyable addition 1+2+3+4+...=-1/12 - Micmaths")
st.video("https://www.youtube.com/watch?v=xqTWRtNDO3U")
