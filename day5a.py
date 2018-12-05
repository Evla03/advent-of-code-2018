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


old_data = None
while data != old_data:
    old_data = data
    data = parse(data)
    # print(len(data))
    # print(data)

# THIS IS REALLY SLOW
print(len(data))
