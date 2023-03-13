def sito(n):
    kandydat = list(range(n+1))
    kandydat.remove(0)
    kandydat.remove(1)
    for dzielnik in kandydat:
        for liczba in kandydat:
            if liczba == dzielnik:
                continue
            if liczba % dzielnik == 0:
                print(f"liczba {liczba}")
                print(f"dzielnik {dzielnik}")
                kandydat.remove(liczba)

    return kandydat

print(sito(100))
