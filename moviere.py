from textblob import TextBlob
import requests
import random
from datetime import datetime
from config import *
from movie_plot_find import *
now = datetime.now()
current_time = now.strftime("%H:%M")
chatbot = "Raspi😊: "
print(f"{chatbot}", current_time)

# TMDB API key (replace 'YOUR_API_KEY' with your actual API key)
# Add your TMDB API key in the config.py file.

if API_KEY == 'use your api key':
    print(chatbot, "You Must Use Your API First")
    print(chatbot, "Make Necessary Adjustments On The (config file) Before Using Me😰")
    exit(0)


def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            print(f"{chatbot}Connection Sucessful...\n")
            return True
    except requests.RequestException:
        pass
    return False

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_feeling():
    print(f"{chatbot}How was your day?")
    user_input = input("You: ")
    sentiment_score = get_sentiment(user_input)
    return sentiment_score
from fetch_movie_rec import*
def provide_movie_recommendation(feeling):
    while True:
        movie_title, movie_release_year, genre, movie_id = get_movie_recommendation(feeling)
        if movie_title is not None:
            print(f"\n{chatbot}Here's a movie recommendation for you:")
            print(f"• Movie Title: '{movie_title}'")
            print(f"• Release Year: '{movie_release_year}'")
            print(f"• Genre: '{genre}'")

            print(f"\n{chatbot}Would you like to know '{movie_title}'s Plot?")
            var1 = input("You: ")
            if var1.lower() in ['yes', 'y']:
                movie_plot = get_movie_plot(movie_id)
                if movie_plot:
                    print(f"{chatbot}The movie starts with {movie_plot}")
                    
                    break
                    
                else:
                    print(f"{chatbot}Sorry, I couldn't fetch the movie plot.")
                    exit
            else:
                break
        else:
            print(f"{chatbot}Sorry, I don't have any movie recommendation right now.")
            break


def main():
    if not check_internet_connection():
        print(f"{chatbot}Sorry, there is no internet connection. Please check your network and try again later.")
        return

    while True:
        sentiment_score = get_feeling()

        if sentiment_score <= -0.5:
            print(f"{chatbot}Sorry to hear that.")
        elif sentiment_score <= 0.5:
            print(f"{chatbot}Feeling neutral?")
        else:
            print(f"{chatbot}Feeling great!")

        provide_movie_recommendation(sentiment_score)
        more_recommendation = input(f"\n{chatbot}Anything else? (yes/no): ")
       
        if more_recommendation.lower() not in ['yes', 'y']:
            break

    find_by_genre = input(f"\n{chatbot}Would you like to find movies by a specific genre? (yes/no): ")
    if find_by_genre.lower() in ['yes', 'y']:
        while True:
            print(f"\n{chatbot}Please tell me the genre you're interested in:")
            genre_name = input("You: ").capitalize()
            if genre_name in genre_polarity_scores:
                movie_title, movie_release_year, genre, movie_id = get_movie_recommendation(genre_polarity_scores[genre_name])
                if movie_title is not None:
                    print(f"\n{chatbot}Here's a {genre} movie for you:")
                    print(f"• Title: '{movie_title}'")
                    print(f"• Release Year: '{movie_release_year}'")
                    print(f"• Genre: '{genre}'")

                    
                    print(f"\n{chatbot}Would you like to know '{movie_title}'s Plot?")
                    var2 = input("You: ")
                    if var2.lower() in ['yes', 'y']:
                        movie_plot = get_movie_plot(movie_id)
                        if movie_plot:
                            print(f"\n{chatbot}{movie_title}'s starts with: {movie_plot}")
                            more_recommendation = input(f"\n{chatbot}Anything else? (yes/no): ")
                        else:
                            print(f"{chatbot}Sorry, I couldn't fetch the movie plot.")
                            break
                    elif var2.lower() in ['no', 'n']:
                        print(f"{chatbot}Okay!, Bye-Bye")
                        break
                    else:
                        print(f"{chatbot}Please answer 'yes' or 'no'.")
                        break
                else:
                    print(f"{chatbot}Sorry, I couldn't find any movies for the genre '{genre_name}'.")
                    break
            else:
                print(f"{chatbot}Sorry, '{genre_name}' is not a valid genre. Please enter a valid genre.")
    elif "exit" in find_by_genre.lower():
        print(f"{chatbot}Bye-Bye")
        exit(0)
    else:
        print(f"{chatbot}Okay!")
        
        

if __name__ == "__main__":
    main()
