n = 100

i = 1
sum = 0
sq_sum = 0
while i <= n:
    print i
    sum = sum + i
    sq_sum = sq_sum + i*i

    i = i + 1


sum = sum*sum

print sq_sum
print sum
print str(sum - sq_sum)
