ponuda = ["Kava", "Topla čokolada", "Nescafe", "Čaj"]
dodaci = {"Kava": ["šećer", "mlijeko"], "Topla čokolada": ["šećer", "med"], "Kakao": ["šećer"], "Čaj": ["šećer" : []}

def meni():
    print("U ponudi imamo: ")
    broj = 0
    for artikl in ponuda:
        broj += 1
        print(str(broj) + ". " + artikl)

#odabir artikla na temelju ponude u listi ponuda[]
def odaberi_artikl():
    while True:
        odabir_artikla = int(input("Unesite redni broj željenog artikla: "))
        if odabir_artikla >= 1 and odabir_artikla <= len(ponuda):
            return odabir_artikla
        else:
            print("Krivo ste unijeli!")

#prikaz dodataka na temelju odabranog artikla
def prikazi_dodatke(odabrani_artikl):
    artikl = ponuda[odabrani_artikl - 1]
    dostupni_dodaci = dodaci[artikl]
    if len(dostupni_dodaci) == 0:
        print("Nema dodataka.")
    else:
        print("Dostupni dodaci: ")
        print("0. ništa")
        broj = 0
        for dodatak in dostupni_dodaci:
            broj += 1
            print(str(broj) + ". " + dodatak)

#odabir dodatka na temelju ponude u mapi dodaci{}
def odaberi_dodatak(odabrani_artikl):
    artikl = ponuda[odabrani_artikl - 1]
    dostupni_dodaci = dodaci[artikl]
    if len(dostupni_dodaci) == 0:
        return 0
    while True:
        odabir_dodatka = int(input("Unesite redni broj željenog dodatka: "))
        if odabir_dodatka >= 0 and odabir_dodatka <= len(dostupni_dodaci):
            return odabir_dodatka
        else:
            print("Krivo ste unijeli!")

def priprema_napitka(odabrani_artikl, odabrani_dodatak):
    artikl = ponuda[odabrani_artikl - 1]
    dostupni_dodaci = dodaci[artikl]
    if odabrani_dodatak == 0:
        print("Priprema se: " + artikl + " bez dodatka.")
    else:
        print("Priprema se: " + artikl + " uz dodatak: " + dostupni_dodaci[odabrani_dodatak - 1] + ".")