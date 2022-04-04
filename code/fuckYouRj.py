import wmi
import speech_recognition as sr
import os
import pyttsx3
import time
import getpass


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


f = wmi.WMI()
while True:
    flag = 0
    for process in f.Win32_Process():
        if "chrome.exe" == process.Name:
            pyttsx3.speak("Rj you moron")
            pyttsx3.speak("Closing google chrome")
            os.system("TASKKILL /F /IM chrome.exe")
            print("Application is Running")
            flag = 1
            break
        if "Discord.exe" == process.Name:
            pyttsx3.speak("Rj fuck you")
            pyttsx3.speak("Closing Discord")
            os.system("TASKKILL /F /IM chrome.exe")
            print("Application is Running")
            flag = 1
            break

    if flag == 0:
        print("Application is not Running")
