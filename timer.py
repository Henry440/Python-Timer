# *-* coding: utf-8 *-*

import time
import os

countspeed = 0.87
schule_pos = 0

def fehler():
    print("Ein Fehler ist Aufgetreten")
    print("kehre zu main zurück")
    time.sleep(2)
    cls()
    main()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def count(sek, minu, stu, mode, end):
    cls()

    sekunde = sek
    minute = minu
    stunde = stu

    mode = mode
    end = end
    global countspeed
    global schule_pos

    aktiv = "true"

    while aktiv:

        time.sleep(countspeed)

        zahl_st1 = ""
        zahl_st2 = ""

        zahl_min1 = ""
        zahl_min2 = ""

        zahl_sek1 = ""
        zahl_sek2 = ""

        sekunde = str(sekunde)
        minute = str(minute)
        stunde = str(stunde)

        
        for i in sekunde:
            sekunde = int(sekunde)
            if sekunde < 10:
                zahl_sek1 = 0
                zahl_sek2 = int(i)
                sekunde = str(sekunde)
            else:
                if zahl_sek1 == "":
                    zahl_sek1 = int(i)
                    sekunde = str(sekunde)
                else:
                    zahl_sek2 = int(i)
                    sekunde = str(sekunde)

        for i in minute:
            minute = int(minute)
            if minute < 10:
                zahl_min1 = 0
                zahl_min2 = int(i)
                minute = str(minute)
            else:
                if zahl_min1 == "":
                    zahl_min1 = int(i)
                    minute = str(minute)
                else:
                    zahl_min2 = int(i)
                    minute = str(minute)

        for i in stunde:
            stunde = int(stunde)
            if stunde < 10:
                zahl_st1 = 0
                zahl_st2 = int(i)
                stunde = str(stunde)
            else:
                if zahl_st1 == "":
                    zahl_st1 = int(i)
                    stunde = str(stunde)
                else:
                    zahl_st2 = int(i)
                    stunde = str(stunde)
            
        sekunde = int(sekunde)
        stunde = int(stunde)
        minute = int(minute)

        
        if mode == 1:
            cls()
            print(zahl_st1, zahl_st2, " : ", zahl_min1, zahl_min2, " : ", zahl_sek1, zahl_sek2)   
        if mode == 2:
            cls()
            print(zahl_st1, zahl_st2, " : ", zahl_min1, zahl_min2)
        if mode == 3:
            cls()
            print(zahl_min1, zahl_min2, " : ", zahl_sek1, zahl_sek2)

            
        if stunde == 0:
            if minute == 0:
                if sekunde == 0:
                    if end == 1:
                        abgelaufen()
                    elif end == 2:
                        schule_pos = schule_pos + 1
                        schule(schule_pos)

        if sekunde > 0:
            sekunde = sekunde - 1
            if sekunde < 0:
                fehler()
        else:
            if sekunde == 0:
                if minute > 0:
                    sekunde = 59
                    minute = minute - 1
                else:
                    if minute == 0:
                        if stunde > 0:
                            stunde = stunde - 1
                            minute = 59
                            sekunde = 59
                        else:
                            if stunde == 0:
                                continue
                

        
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

    if sekunde == 0:
        if minute > 0:
            minute = minute - 1
            sekunde = 60
        else:
            if stunde > 0:
                minute = 59
                sekunde = 60
                stunde = stunde -1
            else:
                cls()
                print("\n" *2)
                print("Die Zeit ist um")
                time.sleep(2)
                abgelaufen()

    end = 1

    count(sek, minu, stu, mode, end)

def abgelaufen():
    cls()

    weiter_inp = 0
    
    while weiter_inp <= 0:
        print("\n" *2)
        print("Die Zeit ist um \n\n")
        print("Wie soll weiter verfahren werden ?")
        print("\n")
    
        print("1) Zum Menü zurück")
        print("2) Normalmodus")
        print("3) Beenden")

        weiter_inp = int(input("> "))
        cls()

    if weiter_inp > 3:
        weiter_inp = 1
        print("Auf Standart (1) gesetzt")
        time.sleep(2)
        cls()

    if weiter_inp == 1:
         main()
    if weiter_inp == 2:
        normal()
    if weiter_inp == 3:
        beenden()
    else:
        main()

            
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
    sek = sekunden_inp

    converter(sek, minu, stu, mode)

def schule(pos):
    cls()

    anweisung = pos
    schule_inp = 0
    
    if anweisung == "main_call":

        while schule_inp <= 0:

            print("\n" *2)
            print("Wie lange ist der Schultag")
            print("")
            print("1) 5 Schulstunden")
            print("2) 6 Schulstunden")
            print("3) 7 Schulstunden")
            print("4) 8 Schulstunden")
            print("")
            print("5) Beenden")
            
            schule_inp = int(input("> "))

        if schule_inp > 5:
            schule_inp = 2
            print("Auf Standart gesetzt (2)")
            time.sleep(2)
            cls()

        
    

def schleife():
    cls()
    pass

def main():
    cls()
    go = "main_call"
    
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
        schule(go)
    elif user_inp == 3:
        schleife()
    elif user_inp == 4:
        beenden()
    else:
        main()
    
main()
