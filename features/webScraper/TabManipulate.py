# # # WEB SCRAPING # # #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand


def newTab(driver):
    driver.execute_script("window.open('');")
    y=len(driver.window_handles)
    y=y-1
    driver.switch_to.window(driver.window_handles[y])
    ''' 
    speak("what do u want me to do now?")
    query = myCommand()
    
    if "open" in query:
        speak("tell me the url")
        tab = myCommand()
        url = "https://www."+tab+".com/"
        speak("opening "+str(tab)+".com")
        #print(url)
        driver.get(url)'''
    #if "close" in query:
       # driver.close()  

def switch_Tab(driver):
    speak("which tab do u want to switch to?")
    query = myCommand()
    if "first" in query:
        driver._switch_to.window(driver.window_handles[0])
    if "second" in query:
        driver._switch_to.window(driver.window_handles[1])
    if "third" in query:
        driver._switch_to.window(driver.window_handles[2])
    if "fourth" in query:
        driver._switch_to.window(driver.window_handles[3])
    if "fifth" in query:
        driver._switch_to.window(driver.window_handles[4])
    if "sixth" in query:
        driver._switch_to.window(driver.window_handles[5])
    if "seventh" in query:
        driver._switch_to.window(driver.window_handles[6])            
    if "eighth" in query:
        driver._switch_to.window(driver.window_handles[7])
    if "ninth" in query:
        driver._switch_to.window(driver.window_handles[8])
    if "tenth" in query:
        driver._switch_to.window(driver.window_handles[9])
    if "eleventh" in query:
        driver._switch_to.window(driver.window_handles[10]) 

    return speak("switched to " +str(driver.title) + " window")

def Open_on_newTab(driver):
    speak("tell me the url")
    tab = myCommand()
    url = "https://www."+tab+".com/"
    speak("opening "+str(tab)+".com")
    #print(url)
    driver.get(url)