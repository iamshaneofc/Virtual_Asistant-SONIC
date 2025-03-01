from voice import speak
import webbrowser
import wikipedia

def open_website(command):
    """Opens a website based on the spoken command."""
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
    }
    
    for site in websites:
        if site in command:
            speak(f"Opening {site}")
            webbrowser.open(websites[site])
            return
    speak("Sorry, I don't know that website.")
    
def google_search(command):
    query = command.replace("search", "").strip()
    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("Please specify what you want to search for.")

def search_wikipedia(query):
    """Searches Wikipedia for a summary of the given query."""
    try:
        summary = wikipedia.summary(query, sentences=2)  # Get a 2-sentence summary
        speak(f"According to Wikipedia: {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"Multiple results found. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak(f"Sorry, I couldn't find any information about {query} on Wikipedia.")
