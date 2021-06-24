# kreiranje i definiranje mapa

mapa_vrijednosti = {"student": True, "ime": "Antonia", "broj_godina": 24}
# dohvaćanje vrijednosti iz mape po ključu
print(mapa_vrijednosti.get("student"))
print(mapa_vrijednosti.get("ime"))
print(mapa_vrijednosti.get("broj_godina"))

#ili
print(mapa_vrijednosti["student"])
print(mapa_vrijednosti["ime"])
print(mapa_vrijednosti["broj_godina"])

# kreiranje / definiranje prazne mape
mapa_vrijednosti = {}
mapa_vrijednosti["spol"] = "Žensko"
print(mapa_vrijednosti["spol"])
mapa_vrijednosti.update({"prezime": "Pesić"})
print(mapa_vrijednosti["prezime"])

# definiranje liste kao vrijednosti
#mapa_vrijednosti["brojevi"] = [1, 2, 3, 4]
#print(mapa_vrijednosti["brojevi"])

# dohvaćanje ključića
for kljuc in mapa_vrijednosti.keys():
    print(kljuc)

# dohvaćanje vrijednosti
for vrijednost in mapa_vrijednosti.values():
    print(vrijednost)

for kljuc in mapa_vrijednosti.keys():
    print(kljuc + " " + mapa_vrijednosti[kljuc])