hz = 0
i = 0
hz_changes = [eval(i) for i in open("input1.txt")]
hz_found = set()

while True:
    hz_found.add(hz)
    i += 1
    hz += hz_changes[i % len(hz_changes) - 1]
    if hz in hz_found:
        print(hz)
        break
