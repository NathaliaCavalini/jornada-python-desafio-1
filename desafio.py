#Primeira fase: import
import pyautogui
import time

pyautogui.PAUSE=1


#Primeiro passo:
pyautogui.press("win") 
pyautogui.write("firefox")
pyautogui.press("enter")


#Segundo passo: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#Terceiro passo: Fazer o login em sí
pyautogui.click(x=491, y=382)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
