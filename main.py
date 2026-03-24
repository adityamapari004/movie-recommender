import streamlit as st
import requests

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    res = requests.get(f"http://127.0.0.1:8000/predict?title={movie}")
    data = res.json()

    for m in data["recommendations"]:
        st.write(m)