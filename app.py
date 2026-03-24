from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd

app = FastAPI()

# Load model
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load final features
with open("final_features.pkl", "rb") as f:
    final_features = pickle.load(f)

# Load data
df = pd.read_csv('clean_netflix.csv')

# --------------------------
# Input Schema
# --------------------------
class InputData(BaseModel):
    title: str

# --------------------------
# Home API
# --------------------------
@app.get("/")
def home():
    return {"message": "Netflix Recommendation API is running"}

# --------------------------
# Predict API (POST)
# --------------------------
@app.post("/predict")
def predict(data: InputData):
    try:
        # Find the index of the title
        if data.title not in df['title'].values:
            return {"error": "Title not found"}
        
        index = df[df['title'] == data.title].index[0]
        
        # Get the feature vector
        input_vector = final_features[index]
        
        # Find nearest neighbors
        distances, indices = model.kneighbors(input_vector, n_neighbors=6)
        
        # Get recommended shows with details (excluding the input itself)
        recommended_indices = indices[0][1:]
        recommendations = []
        for i, dist in zip(recommended_indices, distances[0][1:]):
            show = df.iloc[i]
            recommendations.append({
                "title": show['title'],
                "type": show['type'],
                "director": show['director'],
                "cast": show['cast'],
                "country": show['country'],
                "release_year": int(show['release_year']),
                "rating": show['rating'],
                "listed_in": show['listed_in'],
                "description": show['description'],
                "distance": dist
            })
        
        return {
            "input_title": data.title,
            "recommendations": recommendations
        }

    except Exception as e:
        return {"error": str(e)}

# --------------------------
# Predict API (GET)
# --------------------------
@app.get("/predict")
def predict_get(title: str):
    try:
        # Find the index of the title
        if title not in df['title'].values:
            return {"error": "Title not found"}
        
        index = df[df['title'] == title].index[0]
        
        # Get the feature vector
        input_vector = final_features[index]
        
        # Find nearest neighbors
        distances, indices = model.kneighbors(input_vector, n_neighbors=6)
        
        # Get recommended shows with details (excluding the input itself)
        recommended_indices = indices[0][1:]
        recommendations = []
        for i, dist in zip(recommended_indices, distances[0][1:]):
            show = df.iloc[i]
            recommendations.append({
                "title": show['title'],
                "type": show['type'],
                "director": show['director'],
                "cast": show['cast'],
                "country": show['country'],
                "release_year": int(show['release_year']),
                "rating": show['rating'],
                "listed_in": show['listed_in'],
                "description": show['description'],
                "distance": dist
            })
        
        return {
            "input_title": title,
            "recommendations": recommendations
        }

    except Exception as e:
        return {"error": str(e)}