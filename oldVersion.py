#/usr/python3.5
#-*- coding: utf8 -*-

import time
import os

count = 0.97

def schulzeit():
	pass

def runtime(form, stunde, minute, sekunde):
    global count
	
	#Zeit wird ab hier herunter gezählt

    form = int(form)
    stunde = int(stunde)
    minute = int(minute)
    sekunde = int(sekunde)

    aktiv = True
		
    while aktiv:
        #Zältakt
        time.sleep(count)

        #Null ergänzung
        if sekunde <= 9:
            checkse = "0"
        else:
            checkse = ""

        if minute <= 9:
            checkmin = "0"
        else:
            checkmin = ""

        if stunde <= 9:
            checkst = "0"
        else:
            checkst = ""

        #Format Festlegung + ausgabe
        if form == 1:
            os.system("cls")
            print(checkst, stunde, " : ", checkmin, minute, " : ",checkse, sekunde)
        if form == 2:
            os.system("cls")
            print(checkst, stunde , " : " , checkmin, minute)
        if form == 3:
            os.system("cls")
            print(checkmin, minute, " : ", checkse,  sekunde)

        #Beenden der Schleife
        if stunde == 0:
            if minute == 0:
                if sekunde == 0:
                    aktiv = False

        #Reduzierung der sekunden          
        sekunde = sekunde-1
        if sekunde < 0:
                if minute > 0:
                        minute = minute -1
                        sekunde = 59
                elif stunde > 0:
                        stunde = stunde -1
                        minute = 59
                        sekunde = 59
                else:
                        continue

        #Nachholen der zeit aus Minuten und Stunden
        if minute > 0:
            if sekunde == 0:
                sekunde = 59
                minute = minute -1

        if minute == 0:
            if stunde > 0:
                minute = 59
                stunde = stunde -1
                    
        if stunde == -1:
            print("Fehler btte beenden")
            exitp()
    main()                   
 
def converttime(form, stunde, minute, sekunde):
	
	#Zeit wird in Form gebracht
	form = form
	stunde = int(stunde)
	minute = int(minute)
	sekunde = int(sekunde)
	
	#Zeitformat anpassen
	while sekunde >= 60:
		sekunde = sekunde -60
		if sekunde <= -1:
			print("Fehler btte beenden")
			exitp()
		minute = minute +1
        
	while minute >= 60:
		minute = minute -60
		if minute <= -1:
			print("Fehler bitte beenden")
			exitp()
		stunde = stunde +1

	if sekunde > 0:
		sekunde = 59
		if minute >= 1:
			minute = minute - 1
		elif stunde >=1:
			minute = 59
			stunde = stunde - 1
			if stunde < -1:
				print("Fehler bitte beenden")
				exitp()
        
	#Fehler Filtern
	if sekunde <= -1:
		print("Fehler btte beenden")
		exitp()
        
	if minute <= -1:
		print("Fehler btte beenden")
		exitp()
        
	if stunde <= -1:
		print("Fehler btte beenden")
		exitp()

    #Übergabe
	runtime(form, stunde, minute, sekunde)

def main():
	print("Was möchten sie tun ?")
	print("1) Countdown Starten")
	print("2) Schulmodus")
	print("3) Beenden")
	
	mainauswahl = input("> ")
	mainauswahl = int(mainauswahl)
	
	if mainauswahl > 3:
		main()
	elif mainauswahl == 3:
		exitp()
	elif mainauswahl == 2:
		schulzeit()
	else:
		zeiteingabe()
	
	
def zeiteingabe():
	
	#Start der Eingabe
        print("Bitte geben sie die Zeit ein")
        stunde = int(input("Stunden   : "))
        minute = int(input("Minuten  : "))
        sekunde = int(input("Sekunden : "))

        os.system("cls")
	
	#Format Auswahl
        print("Format wählen")
        print("")
        print("1) hh:mm:ss")
        print("2) hh:mm")
        print("3) mm:ss")
        print("")
    
	#Format Überprüfung
        form = int(input("> "))
        if form > 3:
                print("kein Format hiterlegt '\n' Standart wird gesetzt")
                form = 1
        os.system("cls")
        
    #Übergabe
        converttime(form, stunde, minute, sekunde)

	
def exitp():
	print("Programm wirklich beenden ?")
	print("Beenden? j/n")
	choiceexit = input("> ")
	
	if choiceexit == "j":
		os.system("cls")
		exit()
	else:
		os.system("cls")
		main()

main()
                     
