ones = {}
ones[0] = 0
ones[1] = len("one")
ones[2] = len("two")
ones[3] = len("three")
ones[4] = len("four")
ones[5] = len("five")
ones[6] = len("six")
ones[7] = len("seven")
ones[8] = len("eight")
ones[9] = len("nine")

tens = {}
tens[2] = len("twenty")
tens[3] = len("thirty")
tens[4] = len("forty")
tens[5] = len("fifty")
tens[6] = len("sixty")
tens[7] = len("seventy")
tens[8] = len("eighty")
tens[9] = len("ninety")

s = 0
for i in xrange(1, 10):
    s += ones[i]

s += len("ten")
s += len("eleven")
s += len("twelve")
s += len("thirteen")
s += len("fourteen")
s += len("fifteen")
s += len("sixteen")
s += len("seventeen")
s += len("eighteen")
s += len("nineteen")

for i in xrange(2, 10):
    for j in xrange(10):
        s += (tens[i] + ones[j])

# s equals sum of 1-99
# multiply by 10 for 0, 100, 200, ..., 900
s *= 10



for h in xrange(1, 10):
    s += (100 * (ones[h] + len("hundred")))
    s += (99 * len("and"))

s += (len("one") + len("thousand"))


print s
