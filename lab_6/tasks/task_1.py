"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
import re
import os, sys
import codecs
from decimal import Decimal


os.chdir(os.path.dirname(sys.argv[0]))

def select_animals(input_path, output_path, compressed=False):
    anima = {}
    units = {'mg':0.000001, 'g':0.001, 'Mg':1000, 'kg':1}
    
    with codecs.open(input_path, 'r', encoding='utf8') as myFile:
        header = myFile.readline()
        a = myFile.readlines()

        for elem in a:
            regex = r'([0-9a-z\-]+)(?:,)([0-9\.]+)(?: )([Mmk]{,1}g)(?:,)(\w+)(?:,)(\w+)(?:,)(\w+)(?:\n?)'
            match = re.search(regex, elem)
            #print(match.groups())
            
            id = match.group(1)
            weight = float(match.group(2))
            unit = match.group(3)
            species = match.group(4)
            name = match.group(5)
            gender = match.group(6)

            if gender == 'male': ind = 0
            else: ind = 1

            if species not in anima.keys():
                anima[species]=[None,None]
                anima[species][ind]=match.groups()
            elif anima[species][ind] is None:
                anima[species][ind]=match.groups()
            else:
                    mass_pre = float(anima[species][ind][1])*units[anima[species][ind][2]]
                    mass_cur = weight*units[unit]
                    if mass_cur < mass_pre:
                        anima[species][ind]=match.groups()


        with open(output_path, 'w', encoding='utf8') as myResult:
            if compressed: result="uuid_gender_mass\n"
            else:
                result=header
                result=result[:-1]
            
            sign = ['M','F']

            for ele in sorted(anima.keys()):
                if anima[ele][0][4] < anima[ele][1][4]: order=(0,1)
                else: order=(1,0)
                
                if compressed is False:
                    for which in order:
                        for next in anima[ele][which]:
                            result += next + ","
                            if next is anima[ele][which][1]: result = result[:-1] + " "
                        result = result[:-1] + "\n"
                else:
                    for which in order:
                        result += anima[ele][which][0] +"_"
                        result += sign[which] + "_"
                        num = float(anima[ele][which][1])*units[anima[ele][which][2]]
                        result += '%.3e' % Decimal(num) + "\n"

            myResult.write(result)



if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
