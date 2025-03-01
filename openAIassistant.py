from voice import speak
from openai import OpenAI
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(
    api_key="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",  # Replace with your OpenRouter API key
    base_url="https://openrouter.ai/api/v1")


def process_with_ai(command):
    """Handles AI-based processing of the command."""
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1-distill-llama-70b:free",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide concise and summarized answers."},
                {"role": "user", "content": command},
            ],
        )

        # Debugging: Print the full API response
        print("API Response:", response)  # Add this line to check the raw response
        # Check if the response contains valid data
        if response and response.choices and response.choices[0].message:
            response_text = response.choices[0].message.content
            print(response_text)
            speak(response_text)
        else:
            print("No valid response received.")
            speak("I couldn't get a response. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, I couldn't process your request. Please try again.")

