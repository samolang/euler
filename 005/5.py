
l = range(2, 21)

factors = []

def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1

    return True


n = 1

for i in l:
    if is_prime(i):
        n = n*i
        factors.append(i)

for i in l:
    if n % i == 0:
        continue

    r = i

    print r

    for j in factors:
        if r % j == 0:
            r = r / j

    print "\t" + str(r)

    n = n * r
    factors.append(r)


print n
