def sito(n):
    kandydat = list(range(n+1))
    kandydat.remove(0)
    kandydat.remove(1)
    for dzielnik in kandydat:
        for liczba in kandydat:
            if liczba == dzielnik:
                continue
            if liczba % dzielnik == 0:
                kandydat.remove(liczba)
    return kandydat

def cezar(txt):
    key = -4
    zaszyfrowany_wyraz = ""
    for znak in txt:
        przesunieta = ord(znak) + key
        zaszyfrowany_wyraz += chr(przesunieta)
    print(zaszyfrowany_wyraz)


def anagram():
    with open("C:\\Users\\ADMINISTATOREK\\Desktop\\Anagramy.txt", "r", encoding="UTF-8") as f:
        for line in f:
            if line is None:
                continue
            line = line.replace("\n", "")
            line = line.split(",")
            print(line)
            if (sorted(line[0]) == sorted(line[1])):
                print("jest to anagram")
            else:
                print("nie jest anagramem")


#Palimdrom
#anagram tablica wystapien 
