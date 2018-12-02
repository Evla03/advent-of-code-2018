data = [i.rstrip("\n") for i in open("input2.txt")]

for i in data:
    for j in data:
        tmp = [1 if k != h else 0 for k, h in zip(i, j)]
        if sum(tmp) == 1:
            j = list(j)
            j.pop(tmp.index(1))
            print(''.join(j))
            quit()
