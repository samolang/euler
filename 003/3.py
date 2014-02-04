n = 600851475143
s = n ** 0.5

i = 2
largest_factor = 1
while i < s:
    while n % i == 0:
        print i
        largest_factor = i
        n = n / i
        s = n ** 0.5
    i = i + 1

print ""
print largest_factor
