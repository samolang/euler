
primes = [2]
n = 3
goal = 2000000
while n < goal:
    prime = True
    for i in primes:
        if n % i == 0:
            prime = False
            break

    if prime:
        primes.append(n)


    if n % (goal/100) == 1:
        print n

    n = n + 2
    while n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        n = n + 2

print sum(primes)
