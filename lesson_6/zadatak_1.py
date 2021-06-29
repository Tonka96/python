# TODO: napravite jednostavan program za vođenje trgovine / upravljanje artiklima

UNOS_ARTIKALA = 1
ISPIS_ARTIKALA = 2
KRAJ = 5

class Artikl:
    def __init__(self, _naziv, kolicina, sifra):
        self.naziv = _naziv
        self.kolicina = kolicina
        self.sifra = sifra

lista_artikala = []

print("--------- Trgovina SMS ---------")
print("Meni")
print("1.) Unos artikala")
print("2.) Ispis artikala")
print("3.) TODO: Naplata artikl")
print("4.) TODO: Uredi artikl")
print("5.) KRAJ")
print("--------------------------------")

while True:
    odabrani_meni = int(input("Unesite željenu akciju: "))
    if odabrani_meni == UNOS_ARTIKALA:
        print("Unos novog artikla")
        naziv_artikla = input("Unesite željeni naziv artikla: ")
        kolicina = input("Unesite željenu količinu artikla: ")
        sifra = input("Unesite željenu šifru artikla: ")
        artikl = Artikl(naziv_artikla, kolicina, sifra)
        lista_artikala.append(artikl)

    elif odabrani_meni == ISPIS_ARTIKALA:
        print("Popis artikala")
        print("Naziv \t\t Količina \t\t Šifra")
        for artikl in lista_artikala:
            print(f"{artikl.naziv}\t\t{artikl.kolicina}\t\t\t\t{artikl.sifra}")

    elif odabrani_meni == KRAJ:
        print("Hvala na korištenju! Doviđenja!")
        exit(9)

    else:
        print("Akcija nije podržana!")