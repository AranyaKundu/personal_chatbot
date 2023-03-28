import os
from login import login_details
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login_to_groupMe():
    options = Options()
    # chrome_options.add_argument('--incognito')
    options.add_argument('--disable-blink-features=AutomationControlled')

    # Create service
    s = Service("C://WebDrivers//chromedriver.exe")
    driver = webdriver.Chrome(service = s, options = options) #, options = chrome_options Add incognito option to chrome driver
    driver.maximize_window()

    driver.get("https://web.groupme.com/signin")
    login = login_details()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "signinUserNameInput")))
    element.send_keys(login.username)

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "signinPasswordInput")))
    element.send_keys(login.pwd)
    driver.find_element(By.XPATH, "//button[@type = 'submit']").click()

    input("Press Enter to close the browser") # to ensure that the browser is not closed automatically
    driver.quit()

