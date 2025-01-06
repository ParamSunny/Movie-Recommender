import streamlit as st
import pickle

# Function to recommend movies
def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load the similarity matrix and movie DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Ensure movies_list is a DataFrame
movies = pickle.load(open('movies.pkl', 'rb'))  # Assuming 'movies.pkl' is a DataFrame
movies_list = movies['title'].values  # Extracting movie titles

# Streamlit app UI
st.title("Movie Recommendation System")

# Dropdown to select a movie
selected_movie = st.selectbox(
    'Select a movie:',
    movies_list
)

# Generate recommendations
if st.button('Recommend'):
    try:
        recommend_name = Recommend(selected_movie)
        st.subheader("Similar To Your Selective Movies:")
        for rec_movie in recommend_name:
            st.write(rec_movie)
    except Exception as e:
        st.error(f"An error occurred: {e}")
