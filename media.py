import requests
from voice import speak
import pywhatkit
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def play_on_youtube(command):
    """Plays a song or video on YouTube based on the command."""
    if "play" in command:
        query = command.replace("play", "").strip()  # Extract the song/video name
        speak(f"Playing {query} on YouTube")
        pywhatkit.playonyt(query)
    else:
        speak("Please specify a song or video to play.")

def fetch_movie_details(movie_name):
    """Fetches movie details from TMDb API."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
    response = requests.get(url)
    data = response.json()
    
    if data["results"]:
        movie = data["results"][0]
        title = movie["title"]
        overview = movie["overview"]
        release_date = movie["release_date"]
        speak(f"{title}, released on {release_date}. Overview: {overview}")
    else:
        speak("Sorry, I couldn't find that movie.") 
