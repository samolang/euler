sum = 1000

for i in range(1,sum-1):
    for j in range(1, int((sum - i)/2) + 1):
        k = sum - i - j

        if i*i + j*j == k*k:
            print str(i) + ", " + str(j) + ", " + str(k)
            print i*j*k
        elif i*i + k*k == j*j:
            print str(i) + ", " + str(j) + ", " + str(k)
            print i*j*k
        elif k*k + j*j == i*i:
            print str(i) + ", " + str(j) + ", " + str(k)
            print i*j*k
