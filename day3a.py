import re
from dataclasses import dataclass


@dataclass
class Claim:
    id: int
    x: int
    y: int
    size_x: int
    size_y: int


exp = re.compile(r"#([0-9]+) @ ([0-9]+,[0-9]+): ([0-9]+x[0-9]+)")
data = [exp.findall(i)[0] for i in open("input3.txt")]
patterns = [Claim(int(i[0]), *map(int, i[1].split(",")), *map(int, i[2].split("x"))) for i in [j for j in data]]

claims = set()
doubles = set()
for i in patterns:
    for x in range(i.x, i.x + i.size_x):
        for y in range(i.y, i.y + i.size_y):
            cord = x, y
            if cord not in claims:
                claims.add(cord)
            else:
                doubles.add(cord)

print(len(doubles))
