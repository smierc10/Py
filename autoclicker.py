import pyautogui
import time
import keyboard
run = True
def click(run): 
    time.sleep(2)     
    pyautogui.click()
 
def main(run):
    if run:
        for i in range(30): 
            if keyboard.is_pressed('q'):
                run = False
                print("end")
            else:
                click(run)


main(run)
