
print str(100*100)
print str(999*999)

l1 = range(100, 1000)
l2 = range(100, 1000)
l1.reverse()
l2.reverse()

def is_palindrome(n):
    s = str(n)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1

    return True

a = 0
b = 0
largest = 0
for i in l1:
    for j in l2:
        if is_palindrome(i*j):
            if i*j > largest:
                a = i
                b = j
                largest = i*j

print str(a) + " * " + str(b) + " = " + str(largest)
