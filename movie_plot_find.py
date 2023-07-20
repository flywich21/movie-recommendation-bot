import requests
from config import*
def get_movie_plot(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}',
                            params={'api_key': API_KEY})
    data = response.json()
    if 'overview' in data:
        return data['overview']
    return None