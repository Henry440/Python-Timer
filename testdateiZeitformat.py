import time


zahl = str(42)
zahl1 = ""
zahl2 = ""

for i in zahl:
    if zahl1 == "":
        zahl1 = int(i)
    else:
        zahl2 = int(i)

print(zahl1, zahl2)

time.sleep(4)
