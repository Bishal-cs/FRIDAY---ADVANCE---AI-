"""This Speech to text using selenium and automated chrome browser. this is navigate to a website to speak text"""
import time     
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  # Remove this if you want to see the browser UI

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try: 
    driver.get("https://nethytechtts-reader.netlify.app/")
    
    def speak(text):
        try:
            text_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]')))
            text_box.click()
            text_box.send_keys(text)
            print(f"You said: {text}")

            speak_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]')))
            speak_button.click()

            sleep_duration = min(0.2 + len(text) // 5, 5)
            time.sleep(sleep_duration)
            text_box.clear()

        except Exception as e:
            print(f"An error occurred: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
