print("starting spotIG")
print("made by yzde")
print("--------------------")
print("© yzde")
print("find more abt my projects at yzde.es or my git; yazidears")
print("")
print("")
print("")
print("")
print("starting GUI")
from os import system, name
from instagram_web_api import Client, ClientCompatPatch
import time
import os
#from instagram_private_api import Client
import json
#import colorama
#from colorama import Fore, Back, Style
def gui(name, title, process, text, additional):
    print("")
print("Defining...")
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
print("importing things")
clear()
print("starting spotIG")
print("made by yzde")
print("--------------------")
print("© yzde")
print("find more abt my projects at yzde.es or my git; yazidears")
print("")
print("")
print("")
print("Importing COLORAMA")

clear()
print("starting spotIG")
print("made by yzde")
print("--------------------")
print("© yzde")
print("find more abt my projects at yzde.es or my git; yazidears")
print("")
print("")
print("")
print("starting")
print("getting token and song")
doingso = True
while doingso:
    os.system("python3 stuff/getcurspot.py")
    curr = open("data/currently.yzde", "r")
    dat = curr.read()
    data = ""
    i = 0
    for x in dat:
        break
        i = i + 1
        print("pos="+str(i)+" == "+ dat[(i-1)])
        if x == "'":
            if '"track_name"' in data:
                if '"artists"' in data:
                    x = '"'
                else:
                    x = "'"
            else:
                x = '"'
        data = data + x
    print(dat)
    dat = eval(dat)
    print(str(dat))
    curr.close()
    currtitle = dat.get('track_name')
    currart = dat.get('artists')
    clear()
    print("Listening " + currtitle + " by " + currart)
    

     