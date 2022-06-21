# # # WEB SCRAPING # # #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand

def Click_Searched_Result(driver):
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