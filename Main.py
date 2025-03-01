import os
from take_command import take_command
from dotenv import load_dotenv
from voice import speak
from process_command import process_command

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
YT_KEY = os.getenv("YT_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if __name__ == "__main__":
    speak("Sonic is on standby. Say 'Sonic' to activate.")
    while True:
        wake_word = take_command()

        if any(w in wake_word for w in ["sonic", "hello sonic", "hey sonic"]):  # Only activate when wake word is heard
            speak("Hello, Shane! How can I assist you?")
            
            while True:  # Active mode
                command = take_command(timeout=10)  # Listen with a 10s timeout

                if command:
                    # Normalize the command to remove punctuation and extra spaces
                    normalized = command.lower().strip(",.!? ")
                    
                    # If the command is just the wake word, ignore it
                    if normalized in ["sonic", "hello sonic", "hey sonic"]:
                        print("Wake word repeated; ignoring command.")
                        continue
                    
                    if not process_command(command):  # If process_command returns False, exit
                        exit()
                else:
                    print("No command detected for 10 seconds. Going back to standby mode...")
                    speak("Going back to standby mode.")
                    break  # Exit active mode and return to waiting for the wake word
