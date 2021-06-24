# kalkulator

def zbroji(broj_jedan, broj_dva):
    return broj_jedan + broj_dva

def oduzmi(broj_jedan, broj_dva):
    return broj_jedan - broj_dva

def mnozi(broj_jedan, broj_dva):
    return broj_jedan * broj_dva

def dijeli(broj_jedan, broj_dva):
    if broj_dva > 0:
        return broj_jedan / broj_dva
    else:
        print("Dijelenje s 0 nije dozvoljeno!")

def izracunaj(broj_jedan, broj_dva, operacija):
    return eval(f"{broj_jedan}{operacija}{broj_dva}")