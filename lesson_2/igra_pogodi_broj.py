# igra pogodi broj
# zamisli neki broj te daj korisniku da pogađa

import random
from pathlib import Path


trazeni_broj = random.randint(0, 10)
broj_pokusaja = 0

DEFAULT_VALUE = 1000
FILENAME = 'Najbolji_rezultat.txt'

#napravi prazan file ako ne postoji

print("Meni")
print("-------------------------")
print("Odaberite željenu akciju: ")
print("1.) Nova igra")
print("2.) Ispis rezultata")

izbor_menija = int(input());
path = Path(FILENAME)

if izbor_menija == 1:

    while True:
        ucitani_broj = int(input("Unesite broj: "))
        if ucitani_broj == trazeni_broj:
            print("Bravo pogodio si!")
            print("Trebalo ti je " +str(broj_pokusaja) + " pokušaja da pogodiš")

            #provjeriti da li postoji file
            if path.is_file():
                print(f"Datoteka {FILENAME} postoji")
            else:
                print(f"Datoteka {FILENAME} ne postoji")
                with open(FILENAME, 'w', encoding="utf-8") as file_writer:
                    file_writer.write(str(DEFAULT_VALUE));

            with open(FILENAME, 'r', encoding="utf-8") as file_reader:
                najbolji_rezultat = int(file_reader.read());

            if broj_pokusaja < najbolji_rezultat:
                with open(FILENAME, 'w', encoding="utf-8") as file_writer:
                    file_writer.write(str(broj_pokusaja));
            break

        elif ucitani_broj < trazeni_broj:
            print("Unio si manji broj! Pokušaj opet!")
        elif ucitani_broj > trazeni_broj:
            print("Unio si veći broj! Pokušaj opet!")

        broj_pokusaja += 1

elif izbor_menija == 2:
    #provjeriti da li postoji file

    if path.is_file():
        print(f"Datoteka {FILENAME} postoji")
    else:
        print(f"Datoteka {FILENAME} ne postoji")
        with open(FILENAME, 'w', encoding="utf-8") as file_writer:
            file_writer.write(str(DEFAULT_VALUE));

    with open(FILENAME, 'r', encoding="utf-8") as file_reader:
        najbolji_rezultat = int(file_reader.read());
        if najbolji_rezultat != DEFAULT_VALUE:
            print("Najbolji rezultat je " + str(najbolji_rezultat))