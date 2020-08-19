import PySimpleGUI as sg
from generator import *
import random
from pyperclip import copy


def randomPw():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passLen = 12
    p = "".join(random.sample(s, passLen))
    return p


while True:
    event, values = genWindow.read()

    if event in (None, "exitgen"):
        break

    if event in (None, 'gen'):
        genWindow["generatedPW"].update(randomPw())  # updates the window with the password

    if event in (None, "copy"):
        copy(values["generatedPW"])  # copies the password to the clipboard

