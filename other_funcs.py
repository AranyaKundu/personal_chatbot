import os, pyttsx3, datetime, time, pyaudio, geocoder, random, webbrowser
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# Inititate speech engine: 'SAPI' is default for windows, use 'nsss' for macOS
engine = pyttsx3.init('sapi5')
person = engine.getProperty('voices')
engine.setProperty('voice', person[2].id)
engine.setProperty('rate', 160)

def say_it(audio):
    engine.say(audio)
    engine.runAndWait()

# simple wishes based on time
def small_talks():
    hour = int(datetime.datetime.now().hour)
    intro = "I am chatGPT Lite."
    list_common = ["I am chatGPT Lite, your personal chatbot. How may I help you today?", 
    "Hello, I am chatGPT Lite, your personal chatbot. Is there anything I can help you with?", 
    "Hey, I am chatGPT Lite, your personal chatbot. How's it going?", 
    "Hi! I am chatGPT Lite, your personal chatbot. What brings you here today?", 
    "Hi there, I am chatGPT Lite, your personal chatbot. How can I assist you today?"]

    common = random.choice(list_common)
    if (hour >= 4) and (hour < 12):
        say_it(f"Good Morning. {common}")
    elif (hour >= 12) and (hour < 18):
        say_it(f"Good Afternoon. {common}")
    elif (hour >= 18) and (hour < 23):
        say_it(f"Good Evening. {common}")
    else:
        say_it(f"{intro}Time to Sleep. Good night. I will stay awake for you!")


# set a function that will take commands from the user via speech recognition module, converts them to text and execute them
def command_prompt():
    command = sr.Recognizer()
    with sr.Microphone() as voice_src:
        command.pause_threshold = 1
        audio = command.listen(voice_src)
    try:
        output = command.recognize_google(audio, language='en-us')
    except Exception as e:
        say_it("Sorry, couldn't catch that, can you say that again please!")
        return "None!"
    return output

def get_loc():
    g = geocoder.ip('me')
    say_it(f"my location is {g.latlng}.")


def access_analysis():
    webbrowser.open("http://localhost:8501")
    # s = Service("C://WebDrivers//chromedriver.exe")
    driver = webdriver.Chrome() #, options = chrome_options Add incognito option to chrome driver
    driver.get("http://localhost:8501")

    analysis_tab_link = driver.find_element_by_xpath('//a[text()="Analysis"]')
    # Click the Analysis tab link to access it
    analysis_tab_link.click()
    input("Press Enter to close the browser") # to ensure that the browser is not closed automatically
    driver.quit()

def send_emails():
    s  = Service("C://WebDrivers//chromedriver.exe")
    driver = webdriver.Chrome() #, options = chrome_options Add incognito option to chrome driver
    driver.maximize_window()
    driver.get("https://dome.nd.edu/")
    wait = WebDriverWait(driver, 10)
    iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@class='iframe']")))
    driver.switch_to.frame(iframe)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@style='position: static; width: 100%; height: 100%; padding: 5px;']")))
    # driver.execute_script("arguments[0].click();", element)
    element.click()

    input("Press Enter to exit")
    driver.quit()

