def binarny_built_in():
    #zmiana na binarny systemem wbudowanym
    number = int(input())
    x = bin(number)[2:len(bin(number))]
    print("bin: " + x)

def binarny_made_out():
    #zmiana na binarny systemem napisanym
    x = int(input())
    binarna = []
    liczba = 0
    i = 0
    while x != 0:
        binarna.append(x%2)
        x = x // 2
    print(binarna)
    i = len(binarna) - 1
    while i >= 0:
        liczba = liczba*10 + binarna[i]
        i -= 1
    print(liczba)

def dziesiętny():
    #zamiana binarnego na dziesiętny
    x = int(input())
    liczba = 0
    i = 0
    while x != 0:
        liczba += (x%10)*(2**i)
        i += 1
        x = x//10
    print(liczba)

def sito(n):
    #sito eratostenes
    temp = [1 for x in range (n+1)]
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if j%i == 0:
                temp[j] = 0

    primes = []
    for i in range(2, len(temp)):
        if temp[i] == 1:
            primes.append(i)
    return primes

def sito2(n):
    # sito eratostenes wydajniej
    primes = []
    temp = [True] * (n+1)
    for i in range(2, n):
        if temp[i]:
            primes.append(i)
            for j in range((i*i), n+1, i):
                temp[j] = False

    return primes
