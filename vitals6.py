import os
import time
from getpass import getpass

# \\\\System////
# login settings
user = "Admin"
password = "1234"
rootpassword = "0000"
# color
print("\x1b[0;35m")
# - with colorama code
# -- from colorama import Fore, Style
# -- print(Fore.MAGENTA)
# distro
distro = "Original"
distroversion = "v.1.2"
# load time
loadtime1 = 2
loadtime2 = 2
loadtime3 = 3
loadtime4 = 1
# load text
loadtext1 = "Loading configs..."
loadtext2 = "Loading modules..."
loadtext3 = "Verifying..."
loadtext4 = "Done!"
# logo
logo = """
 ██▒   █▓ ██▓▄▄▄█████▓ ▄▄▄       ██▓      ██████     ██████╗
▓██░   █▒▓██▒▓  ██▒ ▓▒▒████▄    ▓██▒    ▒██    ▒    ██╔════╝
 ▓██  █▒░▒██▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ░ ▓██▄      ███████╗
  ▒██ █░░░██░░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░      ▒   ██▒   ██╔═══██╗
   ▒▀█░  ░██░  ▒██▒ ░  ▓█   ▓██▒░██████▒▒██████▒▒   ╚██████╔╝
   ░ ▐░  ░▓    ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▓▒ ▒ ░    ╚═════╝
   ░ ░░   ▒ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░▒  ░ ░   
     ░░   ▒ ░  ░        ░   ▒     ░ ░   ░  ░  ░     
      ░   ░                 ░  ░    ░  ░      ░     
     ░    
"""
# input
v6input = "V6:\\Home> "
v6rootinput = "V6:\\Root> "
v6pythonmoduleinput = "V6:\\Module\\Python> "
# shutdown settings
shutdownmessage = "Shutting down..."
shutdowntime = 2
# reboot settings
rebootmessage = "Rebooting..."
reboottime = 2
rebootopenfilecommand = "python vitals6.py"

# \\\\Vitals 6////
root = 0
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
print("Vitals 6")
print("Distro: "+distro+" "+distroversion)
print("")
print(loadtext1)
time.sleep(loadtime1)
print(loadtext2)
time.sleep(loadtime2)
print(loadtext3)
time.sleep(loadtime3)
print(loadtext4)
time.sleep(loadtime4)
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

clearConsole()
print(logo)
print("")
print("[Login]")
while(True):
    userlogin = str(input("Username: "))
    if userlogin == user:
        break
    else:
        print("Incorrect username!")
while(True):
    passwordlogin = getpass("Password: ")
    if passwordlogin == password:
        print("Loged!")
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        break
    else:
        print("Incorrect password!")
print(logo)
print("")
while(True):
    if root == 0:
        v6t = str(input(v6input))
    if root == 1:
        v6t = str(input(v6rootinput))
    if root > 1:
        print("Error! Invalid root config!")
    if root < 0:
        print("Error! Invalid root config!")
    if v6t == "exit":
        print(shutdownmessage)
        time.sleep(shutdowntime)
        exit()
    if v6t == "reboot":
        print(rebootmessage)
        time.sleep(reboottime)
        os.system(rebootopenfilecommand)
        exit()
    if v6t == "clear":
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
    if v6t == "use module python":
        print("[Python Module]")
        os.system("python")
        print("")
    if v6t == "use module python3":
        print("[Python3 Module]")
        os.system("python3")
        print("")
    if v6t == "use module python -c":
        print("[Python Module CMD]")
        pythoncommand1 = str(input("Python: "))
        pythoncommand2 = "python -c " + pythoncommand1
        print("")
        os.system(pythoncommand2)
    if v6t == "use module python3 -c":
        print("[Python3 Module CMD]")
        pythoncommand1 = str(input("Python3: "))
        pythoncommand2 = "python3 -c " + pythoncommand1
        os.system(pythoncommand2)
        print("")
    if v6t == "root":
        passwordloginroot = getpass("Root password: ")
        if passwordloginroot == rootpassword:
            root = 1
        else:
            print("Incorrect password!")
        print("")
    if v6t == "home":
        root = 0
    if v6t == "ep":
        ep = str(input("EP: "))
        print("")
        print(ep)
        print("")