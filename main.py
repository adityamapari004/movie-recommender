import streamlit as st
import requests

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    res = requests.get(f"https://movie-recommender-fcqt.onrender.com/recommend?title={movie}")
    print("Status:", res.status_code)
    print("Response:", res.text)

    if res.status_code == 200:
        try:
            data = res.json()
        except ValueError:
            print("error: response is not json")
            data = None
    else:
        print("request failed")
        data = None

    if data and "recommendations" in data:
        for m in data["recommendations"]:
            st.write(m)