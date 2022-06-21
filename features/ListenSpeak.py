# # # TEXT-TO-SPEECH # # #
from gtts import gTTS
import pyttsx3

# # # SPEECH-TO-TEXT # # #
import speech_recognition as sr 
import playsound


# # # VOICE SLECTION AND INITIATION # # # 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty( 'voice', voices[2].id)  

# # # SPEAK FUNTION # # #
def speak(audio):
    print("desktop : " + str(audio))
    engine.say(audio)
    engine.runAndWait()
    return audio

# # # LISTEN FUNTION # # #

def myCommand():
    r = sr.Recognizer()                                     #Initialize the recognizer
    with sr.Microphone() as source:
        print(' listening...')
        r.pause_threshold = 1                               #wait for a second to let the recognizer adjust the  
        r.adjust_for_ambient_noise(source, duration=1)      #energy threshold based on the surrounding noise level 
        audio = r.listen(source)                            #listens for the user's input
        command= ""
        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')

        except sr.UnknownValueError:                        #loop back to continue to listen for commands if unrecognizable speech is received
            print("Your last command couldn't be heard ")
            command = myCommand()

        return command