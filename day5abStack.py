import string

data = open("input5.txt").read()

letters = string.ascii_lowercase


def work(stack: list):
    tmp = zip(sorted((stack[0:2])))
    if tmp[0] in letters.upper() and tmp[1] in letters:
        del stack[0:2]

    stack.append(stack.pop(0))
