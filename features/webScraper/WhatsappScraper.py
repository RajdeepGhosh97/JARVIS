# # # WEB SCRAPING # # #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# # # CUSTOM-MADE IMPORTS # # #
from features.ListenSpeak import speak , myCommand


def Open_WhatsApp(driver):
    speak("opening whatsApp web")
    driver.execute_script("window.open('');")
    y=len(driver.window_handles)
    y=y-1
    driver.switch_to.window(driver.window_handles[y])    
    driver.get("https://web.whatsapp.com/")
    time.sleep(0.5)
    return speak("please scan the Q R code to start a chat") 



def open_Chat(name,driver):
    
    Contract_list = {
            "alivia": "BHOOOOPUUUUU","aritra": "Aritra","anisha": "Anisha",
            "rico": "Rico","banty": "Banty","debo": "Debo",
            "tiyasha": "Tiyasha","ma": "Ma Jio","didi": "Didi",
            "arijit da": "Arijit Da","cgec group":"CGEC SUPER SENIOR!!👑👑",
            "cse important": "CSE Important Notifs","asik": "Asik",
            "maxxy": "Maxxxy ME","trisha": "Trishaaa","ankita": "Ankita",
            "asif": "Asif Raja Cgec","sayan": "Sayan EE", "priyam":"Priyam",
            "sudipta cse": "Sudipta Cse","soyata": "Soyata","rimil":"Rimil",
            "project group": "Final year project","sumouli": "Sumouli"
        }
        
    try:
        for i in Contract_list:
                #print(i)
            if name.lower() == i:
                print(Contract_list[i])
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(Contract_list[i]))
                user.click()
                speak("chat of "+ str(name) +" is opened")
    except:
        speak("unable to find the user")