""" Speech to text using google speech recoginition module"""

import subprocess
try: 
    import speech_recognition as sr #check if installed
except ModuleNotFoundError:
    subprocess.run(['pip', 'install', 'SpeechRecognition']) # install the module
    subprocess.run(['pip', 'install', 'pyaudio'])
    import pyaudio
    import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = False
    r.dynamic_energy_threshold = 500
    r.dynamic_energy_adjustment_damping = 0.8
    r.dynamic_energy_ratio = 0.9
    r.pause_threshold = 0.5
    r.operation_timeout = None
    r.non_speaking_duration = 0.5

    with sr.Microphone() as source:
        print("\033[93mSpeak...\033[0m", flush=True)
        audio = r.listen(source)
        print("\033[93mProcessing...\033[0m", flush=True)
        text = r.recognize_google(audio, language="en-IN")
        print("\033[91mYou said: {}\033[0m".format(text), flush=True)

    return text