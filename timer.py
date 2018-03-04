# *-* coding: utf-8 *-*

import time
import os

countspeed = 0.87

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def count():
    cls()
    global countspeed
    pass

def converter():
    cls()
    pass

def beenden():
    cls()

    user_inp = "y"

    print("\n" *2)
    print("Wollen sie das Programm wirklich Beenden ?")
    print("[y] JA / [n] NEIN")
    print("")

    user_inp = input("> ")
    
    if user_inp == "y":
        cls()
        print("Auf Wiedersehen")
        time.sleep(1.5)
        cls()
        exit()
    else:
        cls()
        main()

def normal():
    cls()
    pass

def schule():
    cls()
    pass

def schleife():
    cls()
    pass

def main():
    cls()
    
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

    if user_inp == 1:
        normal()
    elif user_inp == 2:
        schule()
    elif user_inp == 3:
        schleife()
    elif user_inp == 4:
        beenden()
    else:
        main()
    

main()
