import re


class Guard:
    def __init__(self, id):
        self.id = id
        self.sleepagram = [0 for i in range(60)]

    def sleep(self, start, stop):
        for i in range(start, stop + 1):
            self.sleepagram += 1


exp = re.compile(r"\[[0-9]{4}-[0-9]{2}-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] ([a-zA-Z0-9# ]+)")
exp_begin = re.compile(r"Guard #([0-9]+) begins shift")
data = exp.findall(open("input4.txt").read())
data = [(int(''.join(i[0:3])), int(i[2]), i[3]) for i in data]
data.sort()

guards = [i for i in data]
print(guards)
