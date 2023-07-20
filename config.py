#apis and other configs#
API_KEY = "0d62f66b3d0706e775989e9ff7960fa9"
TMDB_API_URL = "https://api.themoviedb.org/3"

# Sample movie genres and their associated polarity scores
genre_polarity_scores = {
    "Romance": 0.8,
    "Action": 0.4,
    "Mystery": 0.6,
    "Comedy": 0.7,
    "Sci-Fi": 0.3,
    "Fantasy": 0.5,
    "Drama": 0.9,
    "Horror": 0.1,
    "Adventure": 0.4,
    "Thriller": 0.6,
    # Add more genre-polarity mappings here...
}
# Genre names to their corresponding genre IDs mapping (obtained from TMDB API documentation)
genre_ids = {
    "Romance": 10749,
    "Action": 28,
    "Mystery": 9648,
    "Comedy": 35,
    "Sci-Fi": 878,
    "Fantasy": 14,
    "Drama": 18,
    "Horror": 27,
    "Adventure": 12,
    "Thriller": 53,
    # Add more genre mappings here...
}