import streamlit as st
import requests

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    res = requests.get(f"https://movie-recommender-fcqt.onrender.com/recommend?title={movie}")
    data = res.json()

    for m in data["recommendations"]:
        st.write(m)