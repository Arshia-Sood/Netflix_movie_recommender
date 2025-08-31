import streamlit as st
import pickle
import requests
from PIL import Image

st.set_page_config(page_title="Netflix Movie Recommender",layout="centered")
st.title("Netflix Movie Recommendation System")

logo=Image.open("netflix_logo.jpg")
st.image(logo,use_container_width=True)

api_key=st.secrets["TMDB_API_KEY"]
def fetch_poster(movie_title):
    url=f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    data=requests.get(url)
    data=data.json()
    if data["results"]:
        poster_path=data["results"][0]["poster_path"]
        full_path="https://image.tmdb.org/t/p/w500/"+poster_path
        return full_path
    else:
        return "https://via.placeholder.com/300x450.png?text=No+Image"


movies = pickle.load(open("movies.pkl","rb"))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf=TfidfVectorizer(stop_words="english")
tfidf_matrix=tfidf.fit_transform(movies["tags"])
similarity=cosine_similarity(tfidf_matrix)


def recommend(movie):
    movie = movie.lower()
    titles_lower = movies['title'].str.lower()
    
    if movie not in titles_lower.values:
        return ["Movie not found. Please check the title."]
        
    movie_index=titles_lower[titles_lower==movie].index[0]
    distances=similarity[movie_index]

    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_poster=[]

    for i in movies_list:
        title=movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_poster.append(fetch_poster(title))

    return recommended_movies,recommended_poster


selected_movie=st.selectbox("Choose a movie:",sorted(movies["title"].unique()))

if st.button("Recommend"):
    movie_name,movie_poster=recommend(selected_movie)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(movie_poster[i])
            st.markdown(f"{movie_name[i]}")