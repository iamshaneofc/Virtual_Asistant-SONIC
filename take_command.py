import speech_recognition as sr
from voice import speak
# 🔹 Speech Recognition Setup
recognizer = sr.Recognizer()
recognizer.dynamic_energy_threshold = True  # Auto-adjusts sensitivity
recognizer.pause_threshold = 0.5  # Faster response

def take_command(timeout = None):
    """Listens to the user's voice command and returns the recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=0.2)  # Adjust for background noise
        if timeout:  #Active Mode
            print("Sonic is listening... Waiting for activation.")
  
            try:
                audio = recognizer.listen(source,timeout=timeout,phrase_time_limit=3)  # Wait until speech is detected
                command = recognizer.recognize_google(audio, language="en-US").lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                print("No response going bact to standby mode...")
                return None
            except sr.UnknownValueError:
                print("Could not understand audio staying in active mode..")
                return None
            except sr.RequestError:
                print("Chech your internet")
                return ""
            except Exception as e:
                    print(f"Error: {e}")
                    return ""
        else:   #passive mode
            print("Sonic is Inactive waiting for activation.")
            while True:
                try:
                    audio = recognizer.listen(source,timeout=3,phrase_time_limit=3)  # Wait until speech is detected
                    command = recognizer.recognize_google(audio, language="en-US").lower()
                    print(f"You said: {command}")
                    return command
                except sr.UnknownValueError:
                    continue  # Ignore unrecognized speech and keep waiting
                except sr.RequestError:
                    print("Check your internet connection.")
                    speak("Please Check your internet connection.")
                    return ""
                except Exception as e:
                    print(f"Error: {e}")
                    return ""