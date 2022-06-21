'''
######## RAINMETER PROGRAM EXECUTION ###########
import os
x= os.system(r'start E:\Rainmeter\Rainmeter.exe')
a = input()
if a:
    os.system('TASKKILL /F /IM Rainmeter.exe')'''

'''
######## GTTS FOR SPEAK FUNCTION ###########
    text_to_speech = gTTS(text=audio, lang='en-uk')
    r = random.randint(1 , 10000000)
    filename= 'audio-' + str(r) + '.mp3'
    text_to_speech.save(filename)
    playsound.playsound(filename)'''

'''
######## CHATBOT FOR CONVERSATION ###########
# Create a chatbot

bot=ChatBot('Candice')
trainer = ChatterBotCorpusTrainer(bot)        # Create a new trainer for the chatbot
trainer.train("chatterbot.corpus.english")    # Train the chatbot based on the english corpus

#chat feature
while True:
    message=myCommand()
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Candice:',reply)
        speak(str(reply))
    if str(message).strip().lower() =='bye':
        print('Candice: Bye')
        break
    

'''

"""
######## GOOGLE WEB AUTOMATION ###########
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
import time


#PATH = r"C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
"""
"""
def Open_Google():
    speak("opening Google.com")
    driver.get("https://www.google.com/")
    return speak("what do you want me to do now?") 
        
    while True: 

        query_src = myCommand()
        if "search" in query_src:
            speak("what can i search for you?")
            Google_Search(myCommand())
            query_to_do = myCommand()
            
                           
            if "back" in query_to_do:
                driver.back()
                speak("what next?")                    
            if "click" in query_to_do:
                Click_google_src_result()
            if "close" in query_to_do:
                driver.close()
                speak(" Browser Closed ")
                speak(" Disconnecting the server ") 
                break
               
        return speak(" Disconnecting the server ")   
       

def Google_Search(text):
    search = driver.find_element_by_name("q")
    search.clear()
    search.send_keys(text)
    search.send_keys(Keys.RETURN)
    speak("what next?")
    



def Click_google_src_result():
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
                #speak("what next?")
                while 1:
                    x = myCommand()
                    if "click" in x:
                        Click_google_src_result()
                    if "back" in x:
                        driver.back()
                    if "search" in x:
                        speak("what to search now?")
                        Google_Search(myCommand())
                    if "close" in x:
                        driver.close()
                        break
         
    except:
        print("error")

    #return speak(" Browser Closed ")
    return speak("what next?")"""

"""
######## WEATHER INFORMATION ###########
from weather import Weather

if 'current weather in' in command:
    reg_ex = re.search('current weather in (.*)', command)
    if reg_ex:
        city = reg_ex.group(1)
        weather = Weather()
        location = weather.lookup_by_location(city)
        condition = location.condition()
        talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

elif 'weather forecast in' in command:
    reg_ex = re.search('weather forecast in (.*)', command)
    if reg_ex:
        city = reg_ex.group(1)
        weather = Weather()
        location = weather.lookup_by_location(city)
        forecasts = location.forecast()
        for i in range(0,3):
            talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                        'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))
"""


"""
import wolframalpha
import wikipedia
import requests


text = input()
question = text.split(" ")
question = " ".join(question[2:])
try:
    #wolframalpha code here
    Wolframalpha_API = "KTYP34-95YWAAP4GE"
    client = wolframalpha.Client(Wolframalpha_API)
    res = client.query(question)
    answer = next(res.results).text 
    #print("according to wolramalpha "+ answer)
    speak("According to wolframalpha")

except:
    #wikipedia code here
    answer = wikipedia.summary(text , sentences=2)
    #print("according to wikipedia "+ answer)
    speak("According TO wikipedia")

"""
"""
def newTab():

    driver.execute_script("window.open('');")
    y=len(driver.window_handles)
    y=y-1
    driver.switch_to.window(driver.window_handles[y]) 
    speak("what do u want me to do now?")
    query = myCommand()
    if "open" in query:
        speak("tell me the url")
        tab = myCommand()
        url = "https://www."+tab+".com/"
        speak("opening "+str(tab)+".com")
        #print(url)
        driver.get(url)
    if "close" in query:
        driver.close()  


def switch_Tab():
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

    return speak("switched to desired window")
"""

"""
thisdict = {
  "alivia": "BHOOOOPUUUUU",
  "aritra": "Aritra",
  "anisha": "Anisha",
  "rico": "Rico",
  "banty": "Banty",
  "debo": "Debo",
  "tiyasha": "Tiyasha",
  "ma": "Ma Jio",
  "didi": "Didi",
  "arijit da": "Arijit Da",
  "cgec group": "CGEC SUPER SENIOR!!👑👑",
  #"cse group": "",
  "cse important": "CSE Important Notifs",
  "asik": "Asik",
  "maxxy": "Maxxxy ME",
  "trisha": "Trishaaa",
  "ankita": "Ankita",
  "asif": "Asif Raja Cgec",
  "sayan": "Sayan EE",
  "priyam": "Priyam",
  "sudipta cse": "Sudipta Cse",
  "soyata": "Soyata",
  "project group": "Final year project",
  "rimil": "Rimil",
  "sumouli": "Sumouli"
}

name = input()

for i in thisdict:
    #print(i)
    if name.lower() in i:
        print(thisdict[i])
        
"""           
"""
driver.get("https://web.whatsapp.com/")   

#name = input("enter name: ")
#msg = input("enter meg: ")
#count = int(input("number oftimes:"))


while True:
    x =input()
    if "new chat" in x:
        new_chat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
        new_chat.click()
    if "open chat" in x:
        name = input("enter name: ")
        try:
            for i in thisdict:
                #print(i)
                if name.lower() == i:
                    print(thisdict[i])
                    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(thisdict[i]))
                    user.click()
        except:
            print("name not found")            
    if "stop" in x:
        break
#msg_box = driver.find_element_by_class_name("_2S1VP")
#msg_box.send_keys("hello")
print("done succesfully")

"""
"""
import datetime

def current_Time():
    TIME = datetime.datetime.now()
    current=datetime.datetime.now().strftime("%I:%M")
    Date = datetime.date.today().strftime("%A,%d %B, %Y")
    return TIME , Date , current

time , date ,current= current_Time()
print(time.hour)
print(date)

if time.hour >= 12 and time.hour <= 23 :
    print(current +" PM")
else:
    print(current +" AM")"""


import pyowm
import datetime
from pyowm.utils import timestamps
api_key = "37687b68912092ff1c0a57cbf172611f"  #Enter your own API Key

owm_obj=pyowm.OWM(api_key)
mgr = owm_obj.weather_manager()

def Weather_report(place):
    weather_location = mgr.weather_at_place(place)
    #weather_forecast = mgr.forecast_at_place('kolkata','3h')

    weather = weather_location.weather
    #forecast = weather_forecast.forecast

    print("-------- CURRENT WEATHER  ----------")
    #temperature - Get current and today’s min-max temperatures in a location#
    temp_celsius=weather.temperature("celsius")
    print("######## TEMPERATURE ########")
    print(f"Temperature: {temp_celsius['temp']} C")
    print(f"Max-temperature: {temp_celsius['temp_max']} C")
    print(f"Min-temperature: {temp_celsius['temp_min']} C")
    print(f"Temperature-Feel: {temp_celsius['feels_like']} C")

    ### wind - Get current wind info on a location ###
    wind = weather.wind()
    print("######## WIND ########")
    print(f"Wind-Speed: {wind['speed']} m/s")
    print(f"Wind-Angle: {wind['deg']} degree")

    ## rain-dict - Get current rain amount on a location ##
    print("######## CURRENT RAIN AMOUNT ########")
    rain = weather.rain  #Also rain amount is a dict, with keys: 1h an 3h,#containing the mms of rain fallen in the last 1 and 3 hours 
    for r in rain:
        if r is None:
            print("Havn't Rained")
        if r is not None:
            print("Rained: ",r)          



    #### FORCASTING ###
    print()
    print()
    print()
    print("--------- WEATHER FORECAST ---------")

    forecaster = mgr.forecast_at_place('kolkata', '3h')

    ### Is it going to be snowy in the next  days ?###
    print("Will have snow: ",forecaster.will_have_snow())    # False

    ### Is it going to be foggy in the next  days ?###
    print("Will have fog: ",forecaster.will_have_fog()) 


    ###When will the weather be sunny in the next five days?###
    c=0
    for i in forecaster.when_clear():
        c+=1 
        #print(i.detailed_status)
    #print(c)
    if c==0:
        print("No clear sky ")
    if c>0:
        print(f'When will the weather be sunny:  Next {c} days with clear sky')


    ###Get forecasted weather for tomorrow###
    tomorrow_wth = timestamps.tomorrow()   # datetime object for tomorrow
    weather_Tmrw = forecaster.get_weather_at(tomorrow_wth)   
    print("Tomorrow weather forcast: ",weather_Tmrw.detailed_status)

    ###Is it going to rain tomorrow?###
    tomorrow_rn = timestamps.tomorrow()    # datetime object for tomorrow
    Will_Rain = forecaster.will_be_rainy_at(tomorrow_rn)
    print("Will rain tomorrow: ",Will_Rain)

