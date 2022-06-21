import os 
import sys
import time
import random
import datetime
from selenium import webdriver #for web-driver

# # # CHATBOT # # #
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# # # CHATBOT TRAINING # # #
#bot=ChatBot('Candice')
#trainer = ChatterBotCorpusTrainer(bot)        # Create a new trainer for the chatbot
#trainer.train("chatterbot.corpus.english")    # Train the chatbot based on the english corpus

        # # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand
#from FaceID import click_pic, process_face
from features.webScraper.GoogleScraper import Open_Google , Google_Search 
from features.webScraper.YoutubeScraper import Open_youTube , Youtube_search
from features.webScraper.Click import Click_Searched_Result
from features.webScraper.TabManipulate import newTab , switch_Tab ,Open_on_newTab
from features.webScraper.WhatsappScraper import Open_WhatsApp,open_Chat
from features.QuestionAnswer import Q_nd_A


        ## GLOBAL VARIABLES ##
PATH = r"C:\Program Files (x86)\chromedriver.exe" #driver path





def current_Time():
    TIME = datetime.datetime.now().strftime("%H:%M:%S")
    return TIME


'''
speak("LOOKING FOR BIO ID . PLEASE LOOK IN THE WEB CAM FOR VERIFICATION ")
file_name=click_pic()
match = process_face(file_name)
time.sleep(1)


if match.upper()== "UNKNOWN":
    speak("SORRY SIR YOU ARE NOT ALLOWED TO ACCESS ME ")
    sys.exit()  


if match.upper() == "RAJDEEP" :
    speak(" YOUR FACE HAS BEEN VERIFIED ")
    speak(f"HELLO {match} WHAT DO YOU WANT ME TO DO?")
''' 
def main_loop():   
    while True:
        speak()
        speak("tell")
        QUERY = myCommand()                                                                     ## ## ### COMMANDS FOR EXECUTION ### ## ## 

        if "open google" in QUERY:                                                                  # OPEN GOOGLE : opens google.com               
            driver = webdriver.Chrome(PATH) 
            Open_Google(driver)

        if "open youtube" in QUERY:                                                                 # OPEN YOUTUBE : opens youtube.com
            Open_youTube(driver)

        if "open whatsapp" in QUERY:                                                                # OPEN WHATSAPP : opens whatsapp.com
            Open_WhatsApp(driver)

        if "open chat" in QUERY:
            speak("whom do you wanna chat with")
            open_Chat(myCommand(),driver)

        if "new tab" in QUERY:                                                                      # NEW TAB : opens new tab in the browser
            newTab(driver)

        if "switch tab" in QUERY:                                                                   # SWITCH TAB : switch between multiple tab
            switch_Tab(driver)   

        if "ok search" in QUERY:                                                                    # OK SEARCH : search on google.com
            speak("what do you want me to search?")
            Google_Search(myCommand(),driver)


        if "search videos" in QUERY:                                                                # SEARCH VIDEOS : search videos on youtube.com
            speak("what do you want me to search?")
            Youtube_search(myCommand(),driver)

        if "open on tab" in QUERY:
            Open_on_newTab(driver)


        if "click" in QUERY:                                                                        # CLICK : click on any link in the webpage
            Click_Searched_Result(driver)


        if "back" in QUERY:                                                                         # BACK : previous window movement
            driver.back()
            speak("done")

        if "close"in QUERY:                                                                         # CLOSE : close the browser                                                                  
            speak("Disconnecting server")
            speak("Closing Browser")
            driver.quit()

        if "answer" in QUERY:                                                                       # ANSWER : answers the questions
            speak("what do you want to know?")
            Q_nd_A(myCommand())

        if 'stop' in QUERY:                                                                         # STOP : ends the program  
            speak("goodbye an have a nice day")
            sys.exit()     
        #else:
            #reply=bot.get_response(QUERY)
            #speak(str(reply))


main_loop()