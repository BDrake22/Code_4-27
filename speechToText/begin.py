import speech_recognition as sr
import os
import pyttsx3
import webbrowser
from cv2 import *
import time

while True:
    try:
        with sr.Microphone() as source:
            # read the audio data from the default microphone
            r = sr.Recognizer()
            audio_data = r.record(source, duration=3)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            print(text)
            print(text.upper())
        if "JARVIS" in text.upper():
            pyttsx3.speak("Hello Mr. Drake")
            pyttsx3.speak("How can I assist you?")

            workurl = 'https://raimak.sharepoint.com/TeamSite/Lists/2021_2nd_Quarter/AllItems.aspx'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=3)
                print("Recognizing...")
                # convert speech to text
                text = r.recognize_google(audio_data)
                print(text)
                print(text.upper())

            if "RUST" in text.upper():
                pyttsx3.speak("Opening")
                pyttsx3.speak("Rust")
                os.startfile(r'C:\Users\BRAYD\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Rust.url')
            elif "RJ" in text.upper():
                pyttsx3.speak("RJ? Calling 911")
                camera_port = 0
                camera = cv2.VideoCapture(camera_port)
                time.sleep(0.1)  # If you don't wait, the image will be dark
                return_value, image = camera.read()
                cv2.imwrite("opencv.png", image)
                del(camera)
            elif "DEAD" in text.upper():
                pyttsx3.speak("Opening")
                pyttsx3.speak("Left for Dead 2")
                os.startfile(r'C:\Users\BRAYD\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Left 4 Dead 2.url')
            elif "PUMMEL" in text.upper():
                pyttsx3.speak("Opening")
                pyttsx3.speak("Pummel Party")
                os.startfile(r'C:\Users\BRAYD\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Pummel Party.url')
            elif "WORK" in text.upper():
                pyttsx3.speak("Let's do some work")
                os.startfile(r'C:\Users\BRAYD\OneDrive\Desktop\AutoCSA\csa.txt')
                os.chdir(r"C:\Users\BRAYD\OneDrive\Desktop\AutoCSA")
                os.system("start cmd")
                webbrowser.get(chrome_path).open(workurl)
    except:
        continue
