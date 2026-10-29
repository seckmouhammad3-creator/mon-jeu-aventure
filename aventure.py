
import streamlit as st

st.title("🗺️ Mon jeu d'aventure")

st.write("Bienvenue, aventurier !")
st.write("Tu te réveilles dans une forêt mystérieuse.")
st.write("Que veux-tu faire ?")

if st.button("🌲 Explorer la forêt"):
    st.write("Un monstre apparaît devant toi ! 👹")
    st.write("Tu perds une vie.")

if st.button("🕳️ Entrer dans la grotte"):
    st.write("Tu trouves un coffre au trésor ! 💎")
    st.write("Bravo, tu as gagné !")

if st.button("🏞️ Aller vers la rivière"):
    st.write("Tu trouves une épée magique ! ⚔️")



