from weather import get_weather 
from news import get_news
from voice import speak
from websites import open_website, search_wikipedia, google_search
import random
from alarm import set_alarm
from time_date import get_time, get_date
from pc_control import open_application, shutdown_pc, restart_pc, lock_pc 
from media import play_on_youtube, fetch_movie_details
from openAIassistant import process_with_ai

def process_command(command):
    """Processes the user's command using the OpenAI API."""
   # Exit condition
    if "exit" in command or "stop" in command:
        exit_messages = ["Goodbye!", "See you later!", "Take care!"]
        speak(random.choice(exit_messages))
        return False  # Stops the loop
    # Open a website
    elif any(site in command for site in ["google", "youtube", "facebook", "instagram", "twitter"]):
        open_website(command)
    elif "tell me about" in command or "movie" in command:
        movie_name = command.replace("tell me about", "").replace("movie", "").strip()     
        fetch_movie_details(movie_name)
    elif "play" in command:  # New condition for playing on YouTube
        play_on_youtube(command) 
    elif "set alarm for" in command:
        alarm_time = command.replace("set alarm for", "").strip()
        set_alarm(alarm_time)
        return True    
    elif "wikipedia" in command or "search for" in command:
        query = command.replace("wikipedia", "").replace("search for", "").strip()
        search_wikipedia(query) 
    elif "weather in" in command:
        city = command.replace("weather in", "").strip()
        get_weather(city) 
    elif "news" in command or "headlines" in command:
        get_news()
    elif "time" in command and "date" in command:
        get_time()
        get_date()
    elif "time" in command:
        get_time()
    elif "date" in command:
        get_date()
    elif "search" in command:
        google_search(command)

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        open_application(app_name)

    elif "shutdown" in command:
        shutdown_pc()

    elif "restart" in command:
        restart_pc()

    elif "lock pc" in command:
      lock_pc()

    # Default: Process command using AI
    else:
        speak("Wait AI is initializing")
        print ("Sorry for delay....")
        process_with_ai(command)
    return True  # Continue the loop