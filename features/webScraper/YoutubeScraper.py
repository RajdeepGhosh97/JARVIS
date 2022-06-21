# # # WEB SCRAPING # # #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand



def Open_youTube(driver):
    speak("opening Youtube.com")
    try:
        driver.execute_script("window.open('');")
        y=len(driver.window_handles)
        y=y-1
        driver.switch_to.window(driver.window_handles[y])    
        driver.get("https://www.youtube.com/")
        #driver.execute_script("window.open('https://www.youtube.com/', 'new window')")
        
    except:
        speak("unable to open youtube due to some driver issue")
        speak("try again please")
        return

    return speak("which video you want to watch now?")     


def Youtube_search(text,driver):

    search = driver.find_element_by_name("search_query")
    search.clear()
    search.send_keys(text)
    search.send_keys(Keys.RETURN)
    speak("what next?")
