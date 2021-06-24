# 2. TODO učitaj ime, prezime, broj godina od korisnika te pospremi po ključevima u mapu
# 2.1 TODO ispiši unesene podatke


# definiraj mapu
mapa_vrijednosti = {}

# učitaj od korisnika vrijednosti
ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
broj_godina = input("Unesite broj godina: ")

# spremi vrijednosti u mapu
mapa_vrijednosti["ime"] = ime
mapa_vrijednosti["prezime"] = prezime
mapa_vrijednosti["broj_godina"] = broj_godina

# ispiši vrijednosti

print(mapa_vrijednosti.get("ime"))
print(mapa_vrijednosti.get("prezime"))
print(mapa_vrijednosti.get("broj_godina"))

