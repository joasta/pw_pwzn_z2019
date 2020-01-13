"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re
import os, sys
import codecs

os.chdir(os.path.dirname(sys.argv[0]))

def check_animal_list(file_path):
    correct=[0,0]
    with codecs.open(file_path, 'r', encoding='utf8') as myFile:
        header = myFile.readline()
        a = myFile.readlines()
        regex = r'(?:[0-9a-f]{8,8}\-[0-9a-f]{4,4}\-[0-9a-f]{4,4}\-[0-9a-f]{4,4}\-[0-9a-f]{12,12}_)([MF])(?:_\d\.\d{3,3}e[\-+]\d\d)'
        
        for ele in a:
            match = re.search(regex, ele)
            if match is not None:
                if match.group(1) is 'M':
                    correct[1]+=1
                else:
                    correct[0]+=1
        return tuple(correct)




if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
