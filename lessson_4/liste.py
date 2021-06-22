# definiranje/kreiranje lista

broj_godina = 20
ime = "Antonia"

# uglade zagrade

# indexi        0, 1, 2, 3, 4,
lista_godina = [10,20,30,40,50]
print(sum(lista_godina))
print(max(lista_godina))

# dohaćanje elemenata iz liste
print(lista_godina[1])

#dodavanje u listu
lista_godina.append(60)
print("Dodali smo broj " + str(lista_godina[5]))

lista_godina.insert(0,-12)
print(lista_godina[0])

# ispis veličine liste
print(len(lista_godina))

#ispis svih elemenata iz liste
print("Ispis elemenata")
for element in lista_godina:
    print(element)

# ispis preko pozicija/indexa
print("Ispis preko indexa")
for pozicija in range(0, len(lista_godina)):
    print(lista_godina[pozicija])

# ispis slova uz stringa
print("Ispis slova iz stringa")
for slovo in ime:
    print(slovo)