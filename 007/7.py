

primes = [2]
n = 3
goal = 10001
while len(primes) < goal:
    prime = True
    for i in primes:
        if n % i == 0:
            prime = False
            break

    if prime:
        primes.append(n)

    n = n+1

print primes[goal - 1]
