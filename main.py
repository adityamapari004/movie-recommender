import streamlit as st
import requests

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter movie name")

if st.button("Recommend"):
    if not movie.strip():
        st.warning("Please enter a movie name.")
    else:
        try:
            res = requests.get(f"https://movie-recommender-fcqt.onrender.com/predict?title={movie}")
            st.write(f"Status: {res.status_code}")

            if res.status_code == 200:
                try:
                    data = res.json()
                    if data and "recommendations" in data:
                        if data["recommendations"]:
                            for m in data["recommendations"]:
                                st.write(m)
                        else:
                            st.info("No recommendations returned for this title.")
                    elif data and "error" in data:
                        st.error(data["error"])
                    else:
                        st.error("No recommendations found in response.")
                except ValueError:
                    st.error("Response is not valid JSON.")
            else:
                st.error(f"Request failed with status code: {res.status_code}")
        except requests.RequestException as e:
            st.error(f"Error making request: {e}")