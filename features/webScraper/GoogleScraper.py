# # # WEB SCRAPING # # #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand



def Open_Google(driver):
    speak("opening Google.com")
    driver.get("https://www.google.com/")    
    return speak("what do you want me to do now?")

def Google_Search(text,driver):
    search = driver.find_element_by_name("q")
    search.clear()
    search.send_keys(text)
    search.send_keys(Keys.RETURN)
    speak("what next?")

def Click_google_src_result(driver):
    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        all_links = main.find_elements_by_tag_name('a')
        links=[]
        for link in all_links:
            if str(link.text).strip():
                #print(link.text)
                links.append(link)
        speak("what do you want me to click?")
        query_click = myCommand()
        for l in links:
            if query_click in str(l.text).lower():
                #print(l.text)
                l.click()     
    except:
        print("error")

    return speak("what next?")