import re

plik = open('1128_wynik_drums.txt', 'r')
linie = plik.readlines()
plik_wyj = open('PREPROCESSOR_perkusje.txt', 'w')

for line in linie:
    if re.search(r'\S', line):
        plik_wyj.writelines(line)
    else:
        print("Pusta linia")
plik.close()
plik_wyj.close()
