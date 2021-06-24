import racunske_operacije as kalkulator
# from racunske_operacije import *

# kalkulator


prvi_broj = int(input("Unesite prvi broj: "))
drugi_broj = int(input("Unesite drugi broj: "))
operacija = input("Unesite operaciju (+, -, *, /)")

# klasičan način
if operacija == "+":
    print(kalkulator.zbroji(prvi_broj, drugi_broj))

elif operacija == "-":
    print(kalkulator.oduzmi(prvi_broj, drugi_broj))

elif operacija == "*":
    print(kalkulator.mnozi(prvi_broj, drugi_broj))

elif operacija == "/":
    print(kalkulator.dijeli(prvi_broj, drugi_broj))

else:
    print(f"Operacija {operacija} nije podržana!")

# pomoću funkcije eval
print(kalkulator.izracunaj(prvi_broj, drugi_broj, operacija))


