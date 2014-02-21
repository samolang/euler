
cache = {}

def moves(m, n):
    if m == 0 or n == 0:
        return 1

    if (m, n) in cache:
        return cache[(m,n)]

    else:
        m2 = moves(m-1, n)
        n2 = moves(m, n-1)

        total = m2 + n2

        cache[(m,n)] = total
        return total

print moves(20,20)



