import pyautogui
import time

while True:
    x, y = pyautogui.position()
    print(f"Posição atual: X={x:4d}  Y={y:4d}", end="\r")  # \r sobrescreve a linha
    time.sleep(0.2)