import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting.")
            return ""

# Main function to respond to commands
def main():
    speak("Hello, how can I assist you today?")
    
    while True:
        command = listen()
        
        if "hello" in command:
            speak("Hello! How are you?")
        
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I can only respond to simple commands like 'hello' and 'exit'.")

# Run the main function
if __name__ == "__main__":
    main()
