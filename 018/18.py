l = [[3],
    [7,4], \
   [2,4,6], \
  [8,5,9,3]]

l = [[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,04,82,47,65],
[19,01,23,75,03,34],
[88,02,77,73,07,63,67],
[99,65,04,28,06,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66,04,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]]

cache = {}

def max_sum(row, column):
    if row == (len(l) - 1):
        return l[row][column]

    if (row, column) in cache:
        return cache[(row, column)]

    choice_1 = max_sum(row+1, column)
    choice_2 = max_sum(row+1, column+1)

    if choice_1 > choice_2:
        total = choice_1 + l[row][column]
    else:
        total = choice_2 + l[row][column]

    cache[(row, column)] = total
    return total

print max_sum(0,0)
