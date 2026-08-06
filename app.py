import os
import streamlit as st
import pickle
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TMDB API KEY
API_KEY = os.getenv("TMDB_API_KEY")

# Load Data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Fetch Poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

    except Exception:
        pass

    return "https://via.placeholder.com/500x750?text=No+Poster"


# Recommendation Function
def recommend(movie):

    movie_index = movies[
        movies['title'].str.lower() == movie.lower()
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# Streamlit UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select Movie",
    movies['title'].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i in range(len(names)):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])