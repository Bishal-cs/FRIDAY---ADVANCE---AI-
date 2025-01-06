"""This is Speech to text using Vosk speech to text module. This is an offline speech to text module"""
import os 
import sys
import queue 
import subprocess 
try: 
    import sounddevice as sd
    from vosk import Model, KaldiRecognizer
except ModuleNotFoundError: 
    subprocess.run("pip install vosk")
    subprocess.run("pip install sounddevice")

    import sounddevice as sd
    from vosk import Model, KaldiRecognizer

MODEL_PATH = "models\vosk-model-en-us-0.22-lgraph"

if not os.path.exists(MODEL_PATH):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as " + MODEL_PATH)
    exit(1)

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(bytes(indata))

def listen():
    print("Processing audio...")
    partical_text = ""
    with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16', channels=1, callback=callback):
        while True:
            data = audio_queue.get()
            if rec.AcceptWaveform(data):
                finalresult = rec.Result()
                text = eval(finalresult).get("text", "")
                if text:
                    print(f"\r{text}", end="\n")
                return text
            else:
                partical_result = rec.PartialResult()
                word = eval(partical_result).get("partial","")
                if word and word != partical_text:
                    print(f"\r{word}", end="", flush=True)
                    partical_text = word