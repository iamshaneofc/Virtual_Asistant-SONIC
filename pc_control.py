import os
import webbrowser
from voice import speak
def open_application(app_name):
    """Opens common applications based on user request."""
    apps = {
        "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "notepad": "notepad.exe",
        "vs code": "C:/Users/YourUser/AppData/Local/Programs/Microsoft VS Code/Code.exe",
        "calculator": "calc.exe",
    }
    
    if app_name in apps:
        speak(f"Opening {app_name}")
        os.startfile(apps[app_name])
    else:
        speak(f"Sorry, I don't know how to open {app_name}")

def shutdown_pc():
    """Shuts down the PC."""
    speak("Shutting down the PC in 5 seconds.")
    os.system("shutdown /s /t 5")

def restart_pc():
    """Restarts the PC."""
    speak("Restarting the PC.")
    os.system("shutdown /r /t 5")

def lock_pc():
    """Locks the PC."""
    speak("Locking the PC.")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def open_website(website):
    """Opens a website in the default browser."""
    speak(f"Opening {website}")
    webbrowser.open(f"https://{website}.com")
