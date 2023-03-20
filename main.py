def sito(n):
    kandydat = list(range(n+1))
    kandydat.remove(0)
    kandydat.remove(1)
    for dzielnik in kandydat:
        for liczba in kandydat:
            if liczba == dzielnik:
                continue
            if liczba % dzielnik == 0:https://github.com/Prz3mol/Algorytm/blob/main/main.py
                kandydat.remove(liczba)
    return kandydat

def cezar(txt):
    key = -4
    zaszyfrowany_wyraz = ""
    for znak in txt:
        przesunieta = ord(znak) + key
        zaszyfrowany_wyraz += chr(przesunieta)
    print(zaszyfrowany_wyraz)

    
#Palimdrom
#anagram tablica wystapien 
