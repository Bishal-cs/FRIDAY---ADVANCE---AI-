"""This is a speech to text using reverse engineering """
import os
import sys
import time 
import requests
import threading
import subprocess
from typing import Union
try:
    from playsound import playsound
except ModuleNotFoundError:
    subprocess.run("pip install playsound==1.2.2")
    from playsound import playsound

def generate_audio(massage: str,voice :str = "en-IN-Wavenet-B"):
    url: str = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={{{massage}}}"

    headers = {'User-Agent':'Mozilla/5.0(Maciontosh;intel Mac OS X 10_15_7)AppleWebkit/537.36(KHTML,like Gecko)Chrome/119.0.0.0 Safari/537.36'}

    try:
        result = requests.get(url=url, headers=headers)
        return result.content
    except:
        return None

def print_animated_text(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def Co_speak(message: str, voice: str = "en-IN-Wavenet-B", folder: str = "", extension: str = ".mp3") -> Union[None,str]:
    try:
        result_content = generate_audio(message,voice)
        file_path = os.path.join(folder,f"{voice}{extension}")
        with open(file_path,"wb") as file:
            file.write(result_content)
        playsound(file_path)
        os.remove(file_path)
        return None
    except Exception as e:
        print(e)

def speak(text):
    t1 = threading.Thread(target=Co_speak,args=(text,))
    t2 = threading.Thread(target=print_animated_text,args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

