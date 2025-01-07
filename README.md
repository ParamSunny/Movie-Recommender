# Movie-Recommender
## Project Overview
The Movie **Recommendation System** is a machine learning-based application designed to suggest movies to users based on their preferences. The system leverages user interaction data and movie characteristics to provide personalized recommendations, enhancing the user experience by predicting movies they are likely to enjoy.
The project aims to solve the problem of overwhelming choices in large movie libraries by delivering tailored suggestions using advanced recommendation techniques.

## How It Work
Suggests movies based on user preferences, viewing history, or similar user behaviors. The system uses **Pickle** for efficient data handling, storing the movie dataset **(movies.pkl)** and similarity matrix **(similarity.pkl)** for quick retrieval during runtime. Pandas facilitates data manipulation, enabling seamless operations on the movie dataset. When a user selects a movie, the app retrieves its index, identifies the most similar movies using the similarity matrix, and displays the recommendations in a clean, intuitive format.

This combination of technologies ensures an efficient and enjoyable user experience. **Python's versatility, Streamlit's simplicity** for creating web applications, and Pickle's ability to serialize data work together to deliver fast and accurate recommendations. Perfect for movie enthusiasts, this system offers an engaging way to discover new titles and enhance the movie-watching experience.

## Technologies Used

**Programming Languages:-** Python

**Frameworks and Libraries:-** Pandas, NumPy, ATS, SkLearn(CountVectorizer), NLTK, Streamlit.

**Tools:-** PyCharm, Docker

**Docker Image link:-** https://hub.docker.com/repository/docker/sunny783/movies-recommender/general

**Dataset kink:-** https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

## How To Run By Docker ##
**Step 1:-** Download Docker desktop (https://www.docker.com/products/docker-desktop/)

**Step 2:-** Open command prompt on your system.

**Step 3:-** Write this command to run movie-recommender-system.

```
docker run -p 8501:8501 sunny783/movies-recommender
```

**Step 4:-** Open localhost:8501 on your browser OR run by link shown in your command prompt
