from itertools import product
from typing import TypeAlias


point: TypeAlias = tuple[int, int]


def part_1(data: list[str]) -> int:
    def _search(p: point, b: set[point] | None = None) -> int:
        if b is None:
            b = set()
        x = p[0]
        y = p[1]
        v = int(data[x][y])
        if v == 9:
            return 1

        q = 0
        if x + 1 < len(data) and int(data[x + 1][y]) == v + 1 and (x + 1, y) not in b:
            q += _search((x + 1, y), b)
            b.add((x + 1, y))
        if x - 1 >= 0 and int(data[x - 1][y]) == v + 1 and (x - 1, y) not in b:
            q += _search((x - 1, y), b)
            b.add((x - 1, y))
        if (
            y + 1 < len(data[0])
            and int(data[x][y + 1]) == v + 1
            and (x, y + 1) not in b
        ):
            q += _search((x, y + 1), b)
            b.add((x, y + 1))
        if y - 1 >= 0 and int(data[x][y - 1]) == v + 1 and (x, y - 1) not in b:
            q += _search((x, y - 1), b)
            b.add((x, y - 1))
        return q

    heads: list[point] = []
    for x, y in product(range(len(data)), range(len(data[0]))):
        if int(data[x][y]) == 0:
            heads.append((x, y))
    V = 0
    for h in heads:
        v = _search(h)
        V += v
    return V


def part_2(data: list[str]) -> int:
    def _search(p: point) -> int:
        x = p[0]
        y = p[1]
        v = int(data[x][y])
        if v == 9:
            return 1

        q = 0
        if x + 1 < len(data) and int(data[x + 1][y]) == v + 1:
            q += _search((x + 1, y))
        if x - 1 >= 0 and int(data[x - 1][y]) == v + 1:
            q += _search((x - 1, y))
        if y + 1 < len(data[0]) and int(data[x][y + 1]) == v + 1:
            q += _search((x, y + 1))
        if y - 1 >= 0 and int(data[x][y - 1]) == v + 1:
            q += _search((x, y - 1))
        return q

    heads: list[point] = []
    for x, y in product(range(len(data)), range(len(data[0]))):
        if int(data[x][y]) == 0:
            heads.append((x, y))
    V = 0
    for h in heads:
        v = _search(h)
        V += v
    return V


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]

    print(part_1(data))
    print(part_2(data))
