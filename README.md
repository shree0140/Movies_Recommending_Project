# PROJECT:  Movies Recommendation Model.

## Overview:
This project is a Movie Recommender System built using Streamlit that allows users to select a movie and receive recommendations for similar films. It leverages precomputed similarity scores stored in a pickle file to find and recommend the top five movies based on their similarity to the selected title. The system fetches movie posters using the TMDB API and displays them alongside the movie titles. The movie data and similarity matrix are loaded from serialized files, and the entire recommendation process is user-driven through an interactive web interface.

## Application link:
[Movie_Recommendation_Project]()

## Project Details:
- **Framework:**
 Built using Streamlit for creating an interactive web application.

- **Deployment:** 
The application is deployed using Render for public accessibility.

- **User Interaction:**
Users can select a movie from a dropdown list to receive recommendations.
A Streamlit selectbox is used to enable this selection process.

- **Recommendation Logic:**
The system uses a **content based** similarity matrix to recommend movies based on how similar they are to the selected title.
Precomputed similarity scores are stored in a pickle file (similarity.pkl).

- **Poster Fetching:**
For each recommended movie, the system fetches the movie poster using the TMDB API.
The movie ID is used to query the API and retrieve the poster.

- **Data Files:**
movie_dict.pkl: Contains movie metadata (e.g., titles, IDs).
similarity.pkl: Stores precomputed similarity scores between movies.

- **Display:**
Recommendations (titles and posters) are displayed using Streamlit’s column feature.

- **Real-Time API Integration:**
 The system fetches and displays real-time movie posters from The Movie Database (TMDB) API.
