import time
from typing import Optional
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

website_path: str = "https://rtstt-nethytech.netlify.app/"
wait_time: int = 10

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, wait_time)

def stream(content: str):
    print("\033[93mYou said: \033[93m"+ f"{content}", end='\r', flush=True)

def get_text() -> str:
    return driver.find_element(By.ID, "output").get_attribute("value").strip()

def click_start_button():
    start_buitton = wait.until(EC.element_to_be_clickable((By.ID, "startButton")))
    start_buitton.click()

def main() -> Optional[str]:
    driver.get(website_path)
    print("Your Speech to text are ready! Now you can start speaking.")
    click_start_button() 
    
    previous_text = ""
    final_text = ""
    
    while True:
        current_text = get_text()
        
        if current_text and current_text != previous_text:
            stream(current_text)
            previous_text = current_text
        
        if current_text.strip() and current_text != final_text:
            final_text = current_text
            print(f"\033[92mUser: {final_text}\033[0m", end='\r',)
            
        start_button_text = driver.find_element(By.ID, "startButton").text
        if start_button_text.strip().lower() == "start":
            break
        
        time.sleep(1)
        
    return final_text

def listen(prints: bool = False) -> Optional[str]:
    while True:
        result = main()
        if result and len(result) != 0:
            print("\r" + " " * (len(result) + 16) + "\r", end="", flush=True)
            if prints:
                print("\033[92m\rYou Said: " + f"{result}\033[0m\n")
            break
    return result

listen()