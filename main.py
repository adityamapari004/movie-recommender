import streamlit as st
import requests

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    try:
        res = requests.get(f"https://movie-recommender-fcqt.onrender.com/recommend?title={movie}")
        st.write(f"Status: {res.status_code}")
        
        if res.status_code == 200:
            try:
                data = res.json()
                if data and "recommendations" in data:
                    for m in data["recommendations"]:
                        st.write(m)
                else:
                    st.error("No recommendations found in response.")
            except ValueError:
                st.error("Response is not valid JSON.")
        else:
            st.error(f"Request failed with status code: {res.status_code}")
    except requests.RequestException as e:
        st.error(f"Error making request: {e}")