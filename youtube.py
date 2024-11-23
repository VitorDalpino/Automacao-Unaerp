# IMPORTAR BIBLIORECAS
import pyautogui as pg # apelido para chamar depois
import time

# Tempo de pausa
pg.PAUSE = 1 # Pausa de 1  segundo

#Pressionar tecla win
pg.hotkey('win','1')
pg.hotkey('ctrl','t')
pg.write('youtube.com')
pg.press('enter')
time.sleep(3)
pg.press('tab', presses=4, interval=0.5)
pg.write('unaerp')
pg.press('enter')
time.sleep(2)
pg.click(x=720, y=666)              
