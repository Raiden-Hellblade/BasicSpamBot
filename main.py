import pyautogui, time, keyboard
time.sleep(5)
f = open("script.txt", 'r')
for line in f:
    if keyboard.is_pressed('ctrl'):
        break
    pyautogui.typewrite(line)
    time.sleep(0.5)
    pyautogui.press("enter")
    
    
