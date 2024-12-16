from collections import Counter

def part_1(data: list[int]) -> int:
    d = data.copy()
    for _ in range(25):
        new = []
        for r in d:
            s = str(r)
            if r == 0:
                new.append(1)
            elif len(s) % 2 == 0:
                dx, sx = s[: len(s) // 2], s[len(s) // 2 :]
                new.append(int(dx))
                new.append(int(sx))
            else:
                new.append(r * 2024)
        d = new
    return len(d)


def part_2(data: list[int]) -> int:
    d = Counter(data)
    for _ in range(75):
        new = Counter()
        for r in d:
            s = str(r)
            if r == 0:
                new[1] += d[r]
            elif len(s) % 2 == 0:
                dx, sx = s[: len(s) // 2], s[len(s) // 2 :]
                new[int(dx)] += d[r]
                new[int(sx)] += d[r]
            else:
                new[r * 2024] += d[r]
        d = new
    return d.total()


if __name__ == "__main__":
    with open("input.txt") as f:
        data = list(map(int, f.read().strip().split()))

    print(part_1(data))
    print(part_2(data))
