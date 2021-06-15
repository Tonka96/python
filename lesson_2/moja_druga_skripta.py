# od korisnika traži brojeve sve dok korisnik ne upiše no
# kada upiše no, ispiši mu sumu unesenih brojeva

x = "Pero je " + "dobar"
y = 1 + 2
ukupno = 0

while True:
    unesena_vrijednost = input("Unesite vrijednost: ")
    if unesena_vrijednost == "no":
        break

    ukupno = ukupno + int(unesena_vrijednost)
    print(ukupno)

# ista stvar ali sa for petljom
ukupno = 0
# 0, 1, 2, 3, 4
for iteracija in range(5):
    unesena_vrijednost = input("Unesite vrijednost iteracije " + str(iteracija))
    ukupno = ukupno + int(unesena_vrijednost)

print(ukupno)
