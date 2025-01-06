import time
import threading
from UI.Login import login
from STT_EngineS.STT_5 import listen
from TTS_EngineS.TTS_2 import speak
from Web_Automation.web_automate import open_website

# while True:
#     website_name = input("Enter website name: ")
#     open_website(website_name)

def talking_to():
    while True:
        text = listen()
        time.sleep(0.01)
        speak(text)

def main():
    t1 = threading.Thread(target=open_website)
    t2 = threading.Thread(target=talking_to)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
main()