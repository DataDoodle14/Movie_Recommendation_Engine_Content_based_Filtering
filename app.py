import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv  

load_dotenv()

# API_KEY = os.getenv("API_KEY")

# -------------------------------
# Load Data
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

similarity_path = os.path.join(BASE_DIR, "model", "similarity.pkl")
movies_path = os.path.join(BASE_DIR, "model", "movies.pkl")

similarity = pickle.load(open(similarity_path, "rb"))
movies = pickle.load(open(movies_path, "rb"))

# Optimized lookup dictionary (O(1) access)
movie_indices = pd.Series(movies.index, index=movies['title']).to_dict()

# -------------------------------
# Fetch Poster Function
# -------------------------------
PLACEHOLDER = "https://via.placeholder.com/300x450?text=No+Image"

def fetch_poster(movie_id):
    API_KEY = os.getenv('API_KEY')

    # Guard: if key is missing, fail immediately with placeholder
    if not API_KEY:
        st.warning("TMDB API key not found. Posters unavailable.")
        return PLACEHOLDER

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(url, timeout=5)  # timeout prevents hanging
        response.raise_for_status()              # raises on 401, 404, etc.
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return PLACEHOLDER

    except requests.exceptions.Timeout:
        st.error(f"Poster fetch timed out for movie ID {movie_id}")
        return PLACEHOLDER
    except requests.exceptions.HTTPError as e:
        st.error(f"TMDB API error: {e}")  # will show 401 if key is wrong
        return PLACEHOLDER
    except Exception as e:
        st.error(f"Unexpected error fetching poster: {e}")
        return PLACEHOLDER


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend(movie):
    if movie not in movie_indices:
        return []

    movie_index = movie_indices[movie]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [
        {
            "movie_id": movies.iloc[i[0]].movie_id,
            "title": movies.iloc[i[0]].title
        }
        for i in movies_list
    ]


# -------------------------------
# UI Layout
# -------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("Smart Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    if not recommendations:
        st.warning("No recommendations found for this movie.")
    else:
        cols = st.columns(5)
        for idx, movie in enumerate(recommendations):
            with cols[idx]:
                poster = fetch_poster(movie["movie_id"])
                st.image(poster, width=220)
                st.caption(movie["title"])