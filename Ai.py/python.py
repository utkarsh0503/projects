import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the server.")
            return None

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    command = recognize_speech()

    if command:
        print("You said:", command)

        if "hello Z" in command:
            speak("Good morning Boss!")
            
        elif "Z" in command:
            speak("Yes boss how can i help you today!")
            
        elif "how are you" in command:
            speak("Im Good boss! what about u")
            
        elif "I love you" in command:
            speak("Are you a gay!")
            
        elif "who make you" in command:
            speak("My boss utkarsh!")
            
        elif "tell me about yourself" in command:
            speak("Hi my name is z im an personal voice assistant of boss utkarsh !")
            
        elif "today is my birthday wish me" in command:
            speak("happy birthday to you happy birthday to you happy birthday happy birthday happy birthday to you yehhhhh! ")
            
        elif "tell me a joke" in command:
            speak("What do you get a hunter for his birthday? A birthday pheasant")
            speak("Knock! Knock! Who's there? Says. Says who? Says me, that's who")
            speak("Whoever said that the definition of insanity is doing the same thing over and over again and expecting different results has obviously never had to reboot a computer.")
            
        elif "where are u from" in command:
            speak("Im from my home!")
            
        elif "what is computer science" in command:
            speak("According to my knowledge computer science Fundamental areas of computer science Computer science is the study of computation, information, and automation. Computer science spans theoretical disciplines to applied disciplines. Though more often considered an academic discipline, computer science is closely related to computer programming! anything else sir!")
            
        elif "where is your home" in command:
            speak("shut up !")
            
        elif "what are u doing" in command:
            speak("taking with you!")
            
        elif "Which type of food you like" in command:
            speak("I eat internet but my boss love to eat burgers, you want some!")
            
        elif "you love alexa " in command:
            speak("No I am much faster then alexa!")
            
        elif "what is your source of information" in command:
            speak("my source of information is openai!")
       

        elif "what's the time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
            
        elif "Open youtube" in command:
            speak("opening youtube for u boss!")

        elif "stop" in command:
            speak("Bye boss!")
            break

        else:
            speak("I'm sorry, I don't understand that command.")
