import string as strs

data = open("input5.txt").read()

uppercase = strs.ascii_uppercase
lowercase = strs.ascii_lowercase


def parse(string):
    for i in range(len(string)):
        string = list(string)
        tmp = string[i:i + 2]
        tmp = ''.join(sorted(tmp))

        try:
            if tmp[0] in uppercase and tmp[1] in lowercase and tmp[0].lower() == tmp[1].lower():
                del string[i:i + 2]

        except IndexError:
            break

    return ''.join(string)


results = {}
old_data = None
for i in lowercase:
    tmp_data = data

    tmp_data = tmp_data.replace(i, "")
    tmp_data = tmp_data.replace(i.upper(), "")
    print("Removed", i, results)
    while tmp_data != old_data:
        old_data = tmp_data
        tmp_data = parse(tmp_data)
    results[i] = len(tmp_data)
    # print(len(data))
    # print(data)

# THIS IS REALLY, REALLY, REALLY SLOW
print(min(results.values()))
