import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+593969463193')
persona="@jack"
message="manda el mensaje"
sleep(10)

with open('jodete.txt','r') as file:
    for num in range(500):
             pyautogui.typewrite(persona)
             pyautogui.press("enter")
             pyautogui.typewrite(message)
             pyautogui.press("enter")










