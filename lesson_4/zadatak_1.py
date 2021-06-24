# 1. TODO učitaj od korisnika 10 brojeva i spremi u listu
# 1.1 TODO obradi podatke iz liste te ispiši


print("Upiši 10 brojeva: ")

lista = []

for i in range(10):
    broj = int(input("Upišite " + str(i + 1) + " broj: "))
    lista.append(broj)

print("Zbroj brojeva = ", sum(lista))
