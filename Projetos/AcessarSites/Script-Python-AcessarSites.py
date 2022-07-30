#instalações das bibliotecas necessárias, só precisa fazer isso uma vez no computador
#!pip install pyautogui 
#!pip install pyperclip

#responsável pela manipulação do mouse e teclado
import pyautogui
#usa sempre que tiver um caracter especial
import pyperclip
#tempo/dlay entre um comando e outro
import time
#responsável pela manipulação dos dados
import pandas as pd
#executa cada linha de código a cada 1 segundo
pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("google chrome")
#pressiona enter
pyautogui.press("enter")
#abre uma aba
#pyautogui.hotkey("ctrl", "t")
#copia o código
pyperclip.copy("https://drive.google.com/drive/my-drive")
#cola o codigo
pyautogui.hotkey("ctrl","v")
#pressiona enter
pyautogui.press("enter")
#aguarda um tempo pra pagina terminar de carregar
time.sleep(5)
#pega a posição do mouse maaas depende da resolução da tela
#pyautogui.position()
#clica na posição desejada
#clicks = 2, quer dizer para clicar 2x
pyautogui.click(x=392, y=364, clicks = 2)
#aguarda 2 segundos para seguir com o código
time.sleep(2)
#clica nas posições desejadas
#cliqui arquivo
pyautogui.click(x=367, y=361)
#clique : pontos
pyautogui.click(x=1153, y=196)
#clique download
pyautogui.click(x=961, y=590)
#clique fechar
pyautogui.click(x=1342, y=12)

#faz a leitura do arquivo, o 'r' é meio que pra ignorar os caracteres do caminho como '\'
#tabela = pd.read_excel(r"D:\Downloads\Itens a comprar.xlsx")
#mesma coisa que o print, a diferença é que o display é mais bonito
#display(tabela)

#pyautogui.press("win")
#pyautogui.write("google chrome")
#pyautogui.hotkey("ctrl","v")
#pyautogui.press("enter")