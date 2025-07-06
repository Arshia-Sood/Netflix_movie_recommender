# Netflix Movie Recommendation System

A content-based movie recommendation system built using **Python**, **Streamlit**, and **Machine Learning**. This app suggests movies similar to the one you select based on cast, director, genre, and description. Posters are fetched dynamically using the **TMDb API**.



##  Features

-  Search for any movie from Netflix dataset  
-  Get top 5 similar movie recommendations  
-  Movie posters displayed using TMDb API  
-  Clean and interactive interface using Streamlit  
-  Content-based filtering using TF-IDF and Cosine Similarity  



##  How It Works

1. The dataset is preprocessed to create a `tags` column combining key metadata.
2. TF-IDF Vectorization is applied to these tags.
3. Cosine Similarity is calculated to find similar movies.
4. The top 5 matches are shown along with their posters.



##  Project Structure
├── app.py # Streamlit frontend
├── build_model.ipynb # Preprocessing + TF-IDF + similarity calculation
├── movies.pkl # Preprocessed movie data (with tags)
├── netflix_logo.jpg # Banner/logo for UI
├── requirements.txt # Python dependencies
├── .gitignore # To ignore large files like similarity.pkl
└── README.md # Project description



##  Deployment

This app is deployed using **Streamlit Community Cloud**.  
[Live App Link](https://netflixmovierecommender-2uhyf28cjazzafaczdqzwf.streamlit.app/)



Dataset
The dataset used is based on Netflix titles metadata from Kaggle Netflix Dataset.



Author
Arshia Sood
