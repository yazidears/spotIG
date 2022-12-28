print("SetMe for spotIG")
print("made by yzde")
print("--------------------")
print("© yzde")
print("find more abt my projects at yzde.es or my git; yazidears")
print("")
print("")
print("")
print("")
import os
import base64
from os import name, system
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()
dataexists = os.path.exists("data")
if dataexists:
    filesexist = os.path.exists("data/revision.yzde")
    if filesexist:
        print("Checking revision")
        rev = open("data/revision.yzde", "r")
        revdata = rev.read()
        rev.close()
        if revdata == "dosiwpatyzdeu21h769yui34hjeq":
            print("You already set this.")
            print("Adding to that, you need to open 'launcher' for SpotIG to work properly.")
            print("I got u this time tho.")
        elif revdata == "u29riohjbsddas98dshakhefiuefh":
            print("validating.")
            if os.path.exists("data/logdu.encryzde"):
                if os.path.exists("data/logdp.encryzde"):
                    print("decoding")
                    user = open("data/logdu.encryzde", "r")
                    base64_message = user.read()
                    base64_bytes = base64_message.encode('ascii')
                    message_bytes = base64.b64decode(base64_bytes)
                    message = message_bytes.decode('ascii')
                    user.close()
                    user = message
                    passw = open("data/logdp.encryzde", "r")
                    base64_message = passw.read()
                    base64_bytes = base64_message.encode('ascii')
                    message_bytes = base64.b64decode(base64_bytes)
                    message = message_bytes.decode('ascii')
                    passw.close()
                    passw = message
                    print("welcome back, " + user)
                    

                         

