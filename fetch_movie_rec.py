import requests
from config import*
import random
def get_movie_recommendation(feeling):
    genre_scores_diff = {
        genre: abs(polarity_score - feeling)
        for genre, polarity_score in genre_polarity_scores.items()
    }

    best_genre = min(genre_scores_diff, key=genre_scores_diff.get)
    genre_id = genre_ids[best_genre]

    response = requests.get(f'https://api.themoviedb.org/3/discover/movie',
                            params={'api_key': API_KEY, 'with_genres': genre_id})
    data = response.json()

    if 'results' in data:
        movies = data['results']
        if movies:
            movie = random.choice(movies)
            movie_id = movie['id']
            movie_title = movie['title']
            movie_release_year = movie['release_date'][:4]
            return movie_title, movie_release_year, best_genre, movie_id

    return None, None, None, None

