import pyautogui as pg
import time

pg.PAUSE = 1

pg.hotkey('win','1')
pg.hotkey('ctrl','t')
pg.write(r'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/boletim-diario/boletim-diario-do-mercado')
pg.press('enter')
time.sleep(5)

pg.moveTo(x=100, y=100)
pg.scroll(-600)
pg.click(x=390, y=596)
time.sleep(1)
pg.click(x=418, y=680)
time.sleep(2)
pg.hotkey('ctrl','c')
pg.press('enter')

time.sleep(2)


pg.hotkey('ctrl','t')
pg.write(r'https://mail.google.com/mail/u/0/#inbox')
pg.press('enter')
time.sleep(3)

pg.click(x=179, y=207)
time.sleep(3)

pg.write('vitor.dalpino@sou.unaerp.edu.br')
time.sleep(1)
pg.press('enter')
time.sleep(3)
pg.press('tab')

time.sleep(2)
pg.write('Desafio email')


pg.press('tab', presses=4, interval=0.5)
pg.press('enter')

time.sleep(2)
pg.press('enter')
time.sleep(2)
pg.hotkey('ctrl','v')
time.sleep(1)
pg.press('enter')
time.sleep(5)
pg.click(x=1144, y=1034)