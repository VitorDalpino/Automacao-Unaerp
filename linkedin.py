import pyautogui as pg
import time

pg.PAUSE = 0.5
vezes=int(input("Quantas conexões você deseja fazer ? "))

pg.hotkey("Win","1")
pg.hotkey("ctrl","t")
pg.write(r"https://www.linkedin.com/mynetwork")
pg.press('enter')
# time.sleep(7)
# pg.vscroll(-8000)
# time.sleep(3)
# pg.vscroll(-8000)
time.sleep(5)
pg.click(x=1633, y=546)
time.sleep(3)
for i in range(vezes):      
    pg.press('tab', presses=3 , interval=0.5)
    pg.press('enter')
    time.sleep(1)

