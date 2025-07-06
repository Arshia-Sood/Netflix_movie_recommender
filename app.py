import streamlit as st
import pickle

st.set_page_config(page_title="Netflix Movie Recommender",layout="centered")
st.title("Netflix Movie Recommendation System")

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
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


selected_movie=st.selectbox("Choose a movie:",sorted(movies["title"].unique()))

if st.button("Recommend"):
    recommendations=recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for i,movie in enumerate(recommendations,1):
        st.write(f"{i}.{movie}")
