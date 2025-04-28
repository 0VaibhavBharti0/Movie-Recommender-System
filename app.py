import streamlit as st
import pickle
import gdown
import os

# Download similarity.pkl from Google Drive if not already downloaded
file_id = "1NFhWHsSa1pgUyPN4P2d2_dsnFOQU4NAj"  # <-- Replace with your own file id
url = f"https://drive.google.com/uc?id={file_id}"

if not os.path.exists('similarity.pkl'):
    gdown.download(url, 'similarity.pkl', quiet=False)


#Title of the app
st.title("_Movie Recommender_ is :blue[cool] :sunglasses:")

# Load the movies and similarity data
movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_title = movies_list['title'].values

#Recommender function
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)) , reverse=True , key=lambda x:x[1])[1:7]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies_list.iloc[i[0]].title)
    return recommended_movies
        
 #Streamlit interface for movie recommender system       
option = st.selectbox(
    "Select a movie to get recommendations",
    movie_title,
)
if st.button("Recommend", type="primary"):
    recommendation = recommend(option)
    st.subheader("Recommended Movies:")
    for i in recommendation:
        st.write(i)