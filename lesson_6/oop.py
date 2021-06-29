mapa_osobe = {"ime": "", "prezime": ""}
mapa_osobe["ime"] = "Igor"
mapa_osobe["prezime"] = "Znika"

class Osoba:
    def __init__(self, _ime, _prezime):
        self.ime = _ime
        self.prezime = _prezime

    def ispisi_tko_sam(self):
        print("Osoba")

class Zaposlenik(Osoba):
    def __init__(self, _ime, _prezime, _naziv_radnog_mjesta):
        super().__init__(_ime,_prezime)
        self.naziv_radnog_mjesta = _naziv_radnog_mjesta

class Polaznik(Osoba):
    def __init__(self, _ime, _prezime, _naziv_tecaja):
        super().__init__(_ime,_prezime)
        self.naziv_tecaja = _naziv_tecaja

    def upisi_tecaj(self):
        print("Upisao sam tečaj!")

class Auto:
    def __init__(self, _naziv, _boja, _broj_vrata, _broj_kotaca=4):
        self.broj_kotaca = _broj_kotaca
        self.boja = _boja
        self.broj_vrata = _broj_vrata
        self.naziv = _naziv

osoba = Osoba("Igor", "Znika")
auto = Auto("Mercedes", "Zelena", 3);
auto.naziv = "Audi"
print(auto.naziv)
print(auto.broj_kotaca)
print(auto.__dict__)
zaposlenik = Zaposlenik("Pero", "Perić", "Radnik")
print(zaposlenik.__dict__)
polaznik = Polaznik("Ivo", "Ivić", "Python")
print(polaznik.__dict__)
polaznik.upisi_tecaj()
polaznik.ispisi_tko_sam()
zaposlenik.ispisi_tko_sam()
