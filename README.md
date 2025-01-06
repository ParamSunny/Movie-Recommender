# Movie-Recommender
A user-friendly web app built with Python and Streamlit that recommends movies based on your selected title. It uses a pre-trained similarity matrix to suggest the top five similar movies, making discovery fun and efficient for movie lovers

The system uses Pickle for efficient data handling, storing the movie dataset (movies.pkl) and similarity matrix (similarity.pkl) for quick retrieval during runtime. Pandas facilitates data manipulation, enabling seamless operations on the movie dataset. When a user selects a movie, the app retrieves its index, identifies the most similar movies using the similarity matrix, and displays the recommendations in a clean, intuitive format.

This combination of technologies ensures an efficient and enjoyable user experience. Python's versatility, Streamlit's simplicity for creating web applications, and Pickle's ability to serialize data work together to deliver fast and accurate recommendations. Perfect for movie enthusiasts, this system offers an engaging way to discover new titles and enhance the movie-watching experience.

Docker Image link:- https://hub.docker.com/repository/docker/sunny783/movies-recommender/general
