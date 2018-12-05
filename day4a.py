import re
from datetime import datetime
from dataclasses import dataclass


@dataclass
class GuardStatus:
    id: int
    status: int = 0  # 0 = awake, 1 = sleeping


exp = re.compile(r"\[([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})\] ([a-zA-Z0-9# ]+)")
exp_begin = re.compile(r"Guard #([0-9]+) begins shift")
data = exp.findall(open("input4.txt").read())
data = [(datetime.now().strptime(i[0], "%Y-%m-%d %H:%M"), GuardStatus(int(exp_begin.match(i[1]).groups()[0]) if exp_begin.match(i[1]) else None, 0 if i[1] == "wakes up" else 1 if i[1] == "falls asleep" else 0)) for i in data]
data.sort()

for i in range(len(data)):
    if data[i][1].id is None:
        data[i][1].id = data[i - 1][1].id

for i in data:
    print(i)

# for i in data:
#    print(f"{i[0].isoformat()} Guard #{i[1].id}, {'awake' if i[1].status == 0 else 'asleep'}")

guard_minutes = {}

guards = []

for i in data:
    guard_minutes[i[1].id] = [0 for j in range(60)]
    for j in guard_minutes[i[1].id]:
        pass

for i in data:
    if i[1].status == 1:
        for j in guard_minutes[i[1].id]:
            pass

for i in data:
    if i[1].status == 1:
        if i[1].id in guard_minutes:
            guard_minutes[i[1].id][i[0].minute] += 1

        else:
            guard_minutes[i[1].id][i[0].minute] = 1
    else:
        pass


most_asleep = list(guard_minutes.keys())[list(guard_minutes.values()).index(max(guard_minutes.values()))]
out = [(sum(guard_minutes[guard]), max(guard_minutes[guard])) for guard in guard_minutes]
tmp = [x[0] for x in out]
tmp2 = out[tmp.index(max(tmp))]
print(guard_minutes)
print(tmp2[1], most_asleep)
