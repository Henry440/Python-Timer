# *-* coding: utf-8 *-*

import time
import os

countspeed = 0.87

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def count():
    global countspeed
    pass

def converter():
    pass

def beenden():
    pass

def main():

    user_inp = 0

    while user_inp <= 0:
        print("\n"*2)
        print("Modus Wählen")
        print("\n"*2)
        print("1) Normal")
        print("2) Schule")
        print("3) Schleife")
        print("")
        print("4) Beenden")

        user_inp = int(input("> "))
        cls()
 
    if user_inp > 4:
        print("Auf Standart gesetzt (1)")
        time.sleep(2)
        cls()


main()
