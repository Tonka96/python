# kreiranje varijabli
broj_godina = 25
broj_godina_1=1
ukupan_broj_godina = broj_godina + broj_godina_1
print(broj_godina)
print(broj_godina_1)
print(ukupan_broj_godina)

# učitavanje od korisnika

unos_godina = input("Upišite svoj broj godina: ")
print("Upisali ste " + unos_godina)

broj_godina = int(unos_godina)
print("Prvi " + str(broj_godina))

# uvjeti

a = 40
b = 30
if a > b:
    if a > 10:
        print("A je veći od B")
elif a > 1:
    print("A je veći od 1")