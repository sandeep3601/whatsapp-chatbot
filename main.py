import pyautogui
import time
import pyperclip
import ollama

time.sleep(2)

pyautogui.click(x=1072, y=1056)
time.sleep(1) 


pyautogui.moveTo(x=1768, y=930)  
pyautogui.mouseDown()
pyautogui.moveTo(x=702, y=929 , duration=1)  
pyautogui.moveTo(x=702, y=145, duration=1)  
pyautogui.mouseUp
time.sleep(0.5)

pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1426 , 922)

time.sleep(0.5) 

chat_history = pyperclip.paste()

print(chat_history)

response = ollama.chat(
    model="llama3",  
    messages=[
        {
            "role": "system", 
            "content": '''you are a person named sandeep you speak hindi as well as english. you are from india and you are a coder you analyze chat history and respond to the next person like sandeep, do not write time and your name sandeep just give the response of it and give a short response like sandeep , don't use emojis on the end of reply use them in starting. dont repeat the next person reply

                          '''
        },
        {
            "role": "user", 
            "content": chat_history
        }
    ]
)
pyperclip.copy((response['message']['content']))

pyautogui.click(1000,982)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey("enter")
