from datetime import datetime
from voice import speak

def get_time():
    """Fetches and announces the current time."""
    now = datetime.now().strftime("%I:%M %p")  # Format: 12:45 PM
    speak(f"The current time is {now}")
    print(f"🕒 Time: {now}")

def get_date():
    """Fetches and announces the current date."""
    today = datetime.now().strftime("%A, %d %B %Y")  # Format: Monday, 12 February 2025
    speak(f"Today's date is {today}")
    print(f"📅 Date: {today}")
