# primjeri rada sa datotekom
# kada upišemo encoding, onda možemo čitati  č š đ ž ć

# stariji način pisanja
file = open("moja_prva_datoteka.txt", 'w', encoding="utf-8")
file.write("Moja prva datoteka  čšđžć")
file.close()

#noviji način pisanja
with open("moja_druga_datoteka.txt", 'w', encoding="utf-8") as file_writer:
    file_writer.write("Moj tekst")

#n način čitanja - novi
with open("moja_prva_datoteka.txt", encoding="utf-8") as file_read:
    procitana_vrijednost = file_read.read()
    print("Pročitao sam: " + procitana_vrijednost)

# način dodavanja u datoteku - novi
with open("moja_prva_datoteka.txt", 'a', encoding="utf-8") as file_append:
    file_append.write("\nDodavanje novog teksta")

# čitanje iz datoteke koja ne postoji - javlja grešku
with open("moja_prva_datoteka1.txt", encoding="utf-8") as file_read:
    procitana_vrijednost = file_read.read()
    print("Pročitao sam: " + procitana_vrijednost)