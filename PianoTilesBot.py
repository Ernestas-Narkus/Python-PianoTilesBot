import pyautogui
import time
import keyboard
import win32api, win32con

x = 650
y = 300
offset = 100
column = [x, x + offset, x + (2 * offset), x + (3 * offset)]
target_color = (0, 0, 0)

def click(x):
    click_y = y
    win32api.SetCursorPos((x, click_y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def press(key):
    while True:
        if keyboard.is_pressed(key):
            break
        if pyautogui.pixel(column[0], y) == target_color:
            click(column[0])
        elif pyautogui.pixel(column[1], y) == target_color:
            click(column[1])
        elif pyautogui.pixel(column[2], y) == target_color:
            click(column[2])
        elif pyautogui.pixel(column[3], y) == target_color:
            click(column[3])
            
def main():
    key = input("Select letter to being/end the process: ")
    if key.isalpha():
        print("Press the key to begin")
    else:
        print("Not a letter. Retry")
        main()
        
    keyboard.wait(key)
    time.sleep(1)
    press(key)
    
main()