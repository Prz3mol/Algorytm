def sito(n):
    kandydat = [1 for x in range(n+1)]
    pierwsze = []
    for i in range(2,n+1):
        if kandydat[i] != 0:
            pierwsze.append(i)
            for j in range(i+i,n+1,i):
                kandydat[j]=0
    return pierwsze

print(sito(100))
