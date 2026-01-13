#Primeira fase: import
import pyautogui


pyautogui.PAUSE=1


#Primeiro passo:
pyautogui.press("win") 
pyautogui.write("firefox")
pyautogui.press("enter")


#Segundo passo: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
