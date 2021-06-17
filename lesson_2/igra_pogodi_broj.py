# igra pogodi broj
# zamisli neki broj te daj korisniku da pogađa

import random

trazeni_broj = random.randint(0, 10)
broj_pokusaja = 0

while True:
    ucitani_broj = int(input("Unesite broj: "))
    if ucitani_broj == trazeni_broj:
        print("Bravo pogodio si!")
        break
    elif ucitani_broj < trazeni_broj:
        print("Unio si manji broj! Pokusaj opet!")
    elif ucitani_broj > trazeni_broj:
        print("Unio si veci broj! Pokusaj opet!")

    broj_pokusaja += 1

print("Trebalo ti je " + str(broj_pokusaja) + " pokusaja da pogodis")