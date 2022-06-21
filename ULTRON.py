import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty( 'voice', voices[0].id)

#<<< SPEAK FUNCTION >>>
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#<<< WISH FUNCTION >>>
def wish_me():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 4:
        speak(" HI SIR I AM ULTRON ")
        speak(" IT'S BED TIME NOW ")
        
        
    else:
        if hour >= 4 and hour < 12:
            speak("GOOD MORNING SIR ")
        
        elif hour >= 12 and hour < 17:
            speak("GOOD AFTERNOON SIR ")

        else:
            speak("GOOOD EVENING SIR")

    speak("I am Scarlet, a simple but efficient virtual assistant made by a 16 year old programmer in the summer of 2017")
    speak("HOW CAN I HELP U") 

#<<< TAKING COMMAND FUNCTION >>>
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....") 
        query = r.recognize_google(audio, language ='en-us') 
        print("user said: ", query)
        
    except Exception as e:
        #print(e)
        print("Please say that again please...")
        return "None"
    return query


#<<< MAIN FUNCTION >>>
if __name__ == "__main__":
    wish_me()
    while True:       
        query = command().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak("according to wikipedia")
            speak(result)

        elif  'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")   

        elif 'amazon' in query:
            webbrowser.open("amazon.com")

        elif 'music' in query:
            music_dir = 'E:\\SONGS\\Download'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'time' in query:
            TIME = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" sir the time is  {TIME} ")
        
        elif 'stop' in query:
            speak("goodbye")
            sys.exit()