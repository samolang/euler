
def num_divisors(n):
    #print n
    o = n
    primes = {}
    end = int(n**0.5)
    i = 2
    while i <= end:
        if n % i == 0:
            primes[i] = 1
            n = n/i

            while n % i == 0:
                n = n/i
                primes[i] += 1

            end = int(n**0.5)

        i += 1

    if n > 1:
        if n in primes:
            primes[n] += 1
        else:
            primes[n] = 1

    p = 1
    for k in primes.iterkeys():
        v = primes[k]
        #print "\t" + str(k) + ": " + str(v)
        p *= (v + 1)

    #print str(o) + ": " + str(p) + "\n"

    return p

N = 500
n = 0
i = 1
while True:
    n = n + i
    i = i + 1

    if num_divisors(n) > N:
        print n
        break

