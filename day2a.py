import string

twos = 0
threes = 0
for i in open("input2.txt"):
    tmp = [i.count(j) for j in string.ascii_lowercase]
    twos += 1 if 2 in tmp else 0
    threes += 1 if 3 in tmp else 0

print(twos * threes)
