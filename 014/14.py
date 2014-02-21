
max_count = 0
max_n = 0

for i in xrange(1, 1000000):
    n = i
    c = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        c += 1


    if c > max_count:
        max_count = c
        max_n = i

print max_n
