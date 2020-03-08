import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
import time
import re

porter_stemmer = PorterStemmer()
lanca_stemmer = LancasterStemmer()
sb_stemmer = SnowballStemmer("english")
all_tokens = []

plik = open('nazwy_akcesoria.txt', 'r', encoding="utf8")

nazwa = time.time()
nazwa = nazwa.__str__()
nazwa = "nazwy_" + nazwa + ".txt"

plik_wyj = open(nazwa, 'w', encoding="utf8")
word_data = plik.readlines()

for word in word_data:
    nltk_tokens = nltk.word_tokenize(word)
    all_tokens += nltk_tokens

print ('***PorterStemmer****\n')

number_of_stems = 0
all = 0
long = 0
short = 20
stem_length = 0
wyjscie_porter =""
start = time.time()
for w_port in all_tokens:
    if re.search(r'\w', w_port):
        stem = porter_stemmer.stem(w_port)
        print("Actual: %s  || Stem: %s"  % (w_port, stem))
        w_port = w_port.lower()
        plik_wyj.writelines(w_port + '\n')
        plik_wyj.writelines(stem + '\n')
        if w_port != stem:
            number_of_stems = number_of_stems + 1
            stem_length = stem_length + stem.__len__()
        if stem.__len__() > long:
            long = stem.__len__()
        if stem.__len__() < short:
            short = stem.__len__()
        all = all + 1
        wyjscie_porter = wyjscie_porter + stem + " "
    else:
        print("BIALY ZNAK")

stop = time.time()
wynik_czas = stop - start
print ('Czas')
print (wynik_czas)
print ('Suma rdzeni')
print (number_of_stems)
print ('Suma wyrazow')
print (all)
print ('Srednia dlugosc rdzenia')
print (stem_length/number_of_stems)
print ('Najkrotszy rdzen')
print (short)
print ('Najdluzszy rdzen')
print (long)

number_of_stems = 0
all = 0
long = 0
short = 20
stem_length = 0

print ('\n***Paice/HuskStemmer****\n')
start = time.time()
wyjscie_paice = ""
for w_lanca in all_tokens:
    if re.search(r'\w', w_lanca):
            stem = lanca_stemmer.stem(w_lanca)
            print("Actual: %s  || Stem: %s"  % (w_lanca, stem))
            w_lanca = w_lanca.lower()
            plik_wyj.writelines(w_lanca + '\n')
            plik_wyj.writelines(stem + '\n')
            if w_lanca != stem:
                number_of_stems = number_of_stems + 1
                stem_length = stem_length + stem.__len__()
            if stem.__len__() > long:
                long = stem.__len__()
            if stem.__len__() < short:
                short = stem.__len__()
            all = all + 1
            wyjscie_paice = wyjscie_paice + stem + " "
    else:
        print("BIALY ZNAK")

stop = time.time()
wynik_czas = stop - start
print ('Czas')
print (wynik_czas)
print ('Suma rdzeni')
print (number_of_stems)
print ('Suma wyrazow')
print (all)
print ('Srednia dlugosc rdzenia')
print (stem_length/number_of_stems)
print ('Najkrotszy rdzen')
print (short)
print ('Najdluzszy rdzen')
print (long)

number_of_stems = 0
all = 0
long = 0
short = 20
stem_length = 0

print ('\n***SnowballStemmer****\n')
start = time.time()

wyjscie_snowball = ""

for w_snow in all_tokens:
    if re.search(r'\w', w_snow):
        stem = sb_stemmer.stem(w_snow)
        print("Słowo: %s  || Rdzeń: %s"  % (w_snow, stem))
        w_snow = w_snow.lower()
        plik_wyj.writelines(w_snow + '\n')
        plik_wyj.writelines(stem + '\n')
        if w_snow != stem:
            number_of_stems = number_of_stems + 1
            stem_length = stem_length + stem.__len__()
        if stem.__len__() > long:
            long = stem.__len__()
        if stem.__len__() < short:
            short = stem.__len__()
        all = all + 1
        wyjscie_snowball = wyjscie_snowball + stem + " "
    else:
        print("BIALY ZNAK")



stop = time.time()
wynik_czas = stop - start
print ('Czas')
print (wynik_czas)
print ('Suma rdzeni')
print (number_of_stems)
print ('Suma wyrazow')
print (all)
print ('Srednia dlugosc rdzenia')
print (stem_length/number_of_stems)
print ('Najkrotszy rdzen')
print (short)
print ('Najdluzszy rdzen')
print (long)
print("************************************")
print(wyjscie_porter)
print(wyjscie_paice)
print(wyjscie_snowball)

plik.close()
plik_wyj.close()