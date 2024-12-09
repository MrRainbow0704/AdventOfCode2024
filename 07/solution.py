from itertools import product
from pprint import pp


def part_1(data: list[str]) -> int:
    A = set()
    for x0, y0 in product(range(len(data)), range(len(data[0]))):
        if data[x0][y0] == ".":
            continue
        for x1, y1 in product(range(len(data)), range(len(data[0]))):
            if (
                data[x1][y1] == "."
                or (x0, y0) == (x1, y1)
                or data[x0][y0] != data[x1][y1]
            ):
                continue

            dx, dy = x0 - x1, y0 - y1
            if dx >= 0:
                xa = x0 + dx
                xb = x1 - dx
            else:
                xa = x0 - abs(dx)
                xb = x1 + abs(dx)
            if dy >= 0:
                ya = y0 + dy
                yb = y0 - dy
            else:
                ya = y0 - abs(dy)
                yb = y0 + abs(dy)

            if 0 <= xa < len(data) and 0 <= ya < len(data[0]):
                A.add((xa, ya))
            if 0 <= xb < len(data) and 0 <= yb < len(data[0]):
                A.add((xb, yb))
    return len(A)


def part_2(): ...


if __name__ == "__main__":
    with open("sample.txt") as f:
        data = [l.strip() for l in f.readlines()]

    print(part_1(data))
    print(part_2())
