import time

import pyautogui


def mcd_click_draw():
    time.sleep(3)
    x, y = 500, 650
    pyautogui.moveTo(x, y)
    for i in range(10000):
        time.sleep(2)
        pyautogui.click()
        time.sleep(3)
        pyautogui.click()
        print(i)


def fh5_draw():
    time.sleep(2)
    for i in range(3000):
        for j in range(4):
            time.sleep(0.5)
            pyautogui.press('down')
            time.sleep(0.5)

            pyautogui.press('down')
            time.sleep(0.5)

            pyautogui.press('enter')
            time.sleep(0.5)
        print(i)


if __name__ == '__main__':
    fh5_draw()
