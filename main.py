import pyautogui, time, keyboard
time.sleep(5)
f = open("script.txt", 'r')
for word in f:
    if keyboard.is_pressed('ctrl'):
        break
    pyautogui.typewrite(word)
    time.sleep(0.5)
    pyautogui.press("enter")
    
    