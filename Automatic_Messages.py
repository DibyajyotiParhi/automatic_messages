import pyautogui as pg
import time

print("program will run after 5 second")
time.sleep(5)
print("running")

# Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages


for i in range(2):
    pg.write("Hola")
    time.sleep(0.5)
    pg.press("Enter")