import streamlit as st
import pickle 
import pandas as pd
import requests
import time 

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')


def fetch_poster(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2a7f1af4f36fc14b8aba3d52c1a36f45&language=en-US'.format(movie_id))
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        data = response.json()
        if data.get('poster_path') is None:
            return None
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
        time.sleep(1)  # Add a delay to prevent rate limiting
    return recommended_movies, recommended_movies_posters

selected_movie_name = st.selectbox(
'Type or select a movie',
movies['title'].values
)


if st.button('Recommend Movies'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        if posters[0] is not None:
            st.image(posters[0])
        else:
            st.text("Poster not available")
    with col2:
        st.text(names[1])
        if posters[1] is not None:
            st.image(posters[1])
        else:
            st.text("Poster not available")
    with col3:
        st.text(names[2])
        if posters[2] is not None:
            st.image(posters[2])
        else:
            st.text("Poster not available")
    with col4:
        st.text(names[3])
        if posters[3] is not None:
            st.image(posters[3])
        else:
            st.text("Poster not available")
    with col5:
        st.text(names[4])
        if posters[4] is not None:
            st.image(posters[4])
        else:
            st.text("Poster not available")

