import time
import threading
from voice import speak
import re

def convert_to_24_hour(time_str):
    """Converts '7:30 AM' or '7:30 PM' format into 24-hour format."""
    match = re.match(r"(\d{1,2}):(\d{2})\s*(AM|PM|am|pm)?", time_str)
    
    if not match:
        speak("Invalid time format. Please say the time in HH:MM AM or PM format.")
        return None

    hours, minutes, period = match.groups()
    hours, minutes = int(hours), int(minutes)

    if period:
        period = period.upper()
        if period == "PM" and hours != 12:
            hours += 12
        elif period == "AM" and hours == 12:
            hours = 0  # Convert 12 AM to 00:00

    return f"{hours:02}:{minutes:02}"

def set_alarm(alarm_time):
    """Sets an alarm for the specified time (HH:MM AM/PM or 24-hour format)."""
    alarm_time = convert_to_24_hour(alarm_time)  # Convert AM/PM format if needed
    if not alarm_time:
        return
    
    hours, minutes = map(int, alarm_time.split(":"))
    now = time.localtime()
    alarm_seconds = (hours * 3600 + minutes * 60) - (now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec)

    if alarm_seconds < 0:
        speak("The time has already passed for today. Set an alarm for tomorrow instead.")
        return

    speak(f"Alarm set for {alarm_time}.")
    threading.Timer(alarm_seconds, ring_alarm).start()

def ring_alarm():
    """Function to trigger when alarm time is reached."""
    speak("Time's up! Your alarm is ringing!")
    for _ in range(5):  # Beeps 5 times
        print("\a")  # Makes a beep sound (Windows only)
        time.sleep(1)
