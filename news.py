import requests
from voice import speak

COUNTRY = "us"
API_KEY = "4c4ca5a567f84987b67c7c1a7526ce38"

def get_news():
    """Fetches and speaks top news headlines for the specified country."""
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news,cnn&apiKey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            speak("Sorry, no news articles found.")
            print("No news articles available.")
            return

        speak("Here are the latest news headlines.")
        print("Latest News Headlines:\n")

        for article in articles[:5]:  # Limit to first 5 headlines
            print(article['title'])
            speak(article['title'])

    else:
        speak("I couldn't fetch the news at the moment. Please try again later.")
        print(f"Failed to retrieve news. Status Code: {response.status_code}")
