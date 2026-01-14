import pyautogui
import time
import pandas as pd

# Configurações iniciais - mais lento = mais confiável
pyautogui.PAUSE = 0.8          # Aumentei pra dar tempo do navegador reagir
pyautogui.FAILSAFE = True      # Mova mouse pro canto superior esquerdo pra parar o script

# ================================================
# Passo 1 - Abrir navegador e entrar no site
# ================================================
pyautogui.press("win")
time.sleep(0.8)
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(4)  # firefox pode demorar pra abrir

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)  # tempo pra carregar a página de login

# Garantir foco na janela (clica no meio da tela)
screen_width, screen_height = pyautogui.size()
pyautogui.click(screen_width // 2, screen_height // 2)
time.sleep(0.8)

# ================================================
# Passo 2 - Fazer login
# ================================================
pyautogui.click(x=491, y=382)          # campo email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")

pyautogui.write("sua senha")           # ← COLOQUE A SENHA REAL AQUI!

pyautogui.click(x=689, y=536)          # botão entrar
time.sleep(8)  # Aumentado! A página de cadastro demora mesmo pra carregar tudo

# Garantir foco novamente após login
pyautogui.click(screen_width // 2, screen_height // 2)
time.sleep(1)

# ================================================
# Passo 3 - Carregar tabela
# ================================================
tabela = pd.read_csv("produtos.csv")
print(tabela)  # debug, pode remover depois

# ================================================
# Passo 4 - Cadastrar produtos (parte corrigida)
# ================================================
for linha in tabela.index:
    print(f"Cadastrando {linha + 1}/{len(tabela)} → Código: {tabela.loc[linha, 'codigo']}")
    
    # Clique forçado com moveTo + click separado
    pyautogui.moveTo(415, 257, duration=0.3)
    time.sleep(0.2)
    pyautogui.click()
    
    time.sleep(0.8)  # pausa antes de digitar
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    time.sleep(0.2)
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    
    pyautogui.press("tab")
    time.sleep(0.3)
    pyautogui.press("enter")
    
    time.sleep(2.5)  # espera mais o cadastro salvar
    
    pyautogui.scroll(5000)
    time.sleep(1.0)