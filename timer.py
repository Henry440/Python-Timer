# *-* coding: utf-8 *-*

import time
import os

countspeed = 0.87

def fehler():
    print("Ein Fehler ist Aufgetreten")
    print("kehre zu main zurück")
    time.sleep(2)
    cls()
    main()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def count():
    cls()
    global countspeed
    pass

def converter(sek, minu, stu, mode):
    cls()

    sekunde = sek
    minute = minu
    stunde = stu

    mode = mode

    while sekunde > 59:
        sekunde = sekunde -60
        if sekunde < 0:
            fehler()
        else:
            minute = minute + 1

    while minute > 59:
        minute = minute - 60
        if minute < 0:
            fehler()
        else:
            stunde = stunde +1

    if sekunde < 0:
        fehler()
    if minute < 0:
        fehler()
    if stunde < 0:
        fehler()

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

    print("\n" *2)
    print("Bitte die Zeit eingeben")
    print("\n" *1)

    stunden_inp = int(input("Stunden : "))
    print("\n")
    minuten_inp = int(input("Minuten : "))
    print("\n")
    sekunden_inp = int(input("Sekunden : "))
    print("\n")

    cls()

    print("\n" *2)
    print("Zeitformat Wählen")
    print("\n" *2)

    form_inp = 0
    
    while form_inp <= 0:

        print("1) hh:mm:ss")
        print("2) hh:mm")
        print("3) mm:ss")

        print("4) Programm Beenden")

        form_inp = int(input("> "))
        cls()

    if form_inp > 4:
        form_inp = 1
        print("Auf Standart gesetzt (1)")
        time.sleep(2)
        cls()

    mode = form_inp
    stu = stunden_inp
    minu = minuten_inp
    sek = sekunden _inp

    converter(sek, minu, stu, mode)

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
        user_inp = 1
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
