class działanie():
    def dowolny(x,system):
        #zamiana z dowolnego systemu binarnego
        liczba = 0
        i = 0
        while x != 0:
            liczba += (x%10)*(system**i)
            i += 1
            x //= 10

        print(liczba)
        return liczba

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
    
    def standard_deviation(n):
        
    """V is list of variables (originally I needed velocity that's why v)
       Vs is sum of variables
       sumapoteg is sum of tbh idk what, I suck at math
       n is ammount of variables to declare"""
        import math as m
        v = []
        vs = 0
        sumapoteg = 0
        #n = int(input())


        #creates list of variables
        #I used float in case it was needed
        i = 0
        while i != n:
            v.append(float(input()))
            i += 1
            print(i,n,v)

        #sums up variables
        #after loop vs becomes averege of variables
        k = 0
        while k != n:
            vs += v[k]
            k += 1
        vs /= n

        #now this one sums powers of idk some math bs
        j = 0
        while j != n:
            sumapoteg += ((v[j]-vs)*(v[j]-vs))
            j += 1

        #print((vs, n, v, sumapoteg/n))

        wynik = m.sqrt((sumapoteg/n))
        return wynik
