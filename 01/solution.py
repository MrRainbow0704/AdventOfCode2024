from collections import Counter

def part_1(l1: list[int], l2: list[int]) -> int:
    d = 0
    for a, b in zip(sorted(l1), sorted(l2)):
        d += abs(a - b)
    return d


def part_2(l1: list[int], l2: list[int]) -> int:
    s = 0
    c = Counter(l2)
    for a in l1:
        s += a * c[a]
    return s


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [(a, b) for a, b in map(lambda x: x.split(), f.readlines())]
        A = [int(a) for a, _ in data]
        B = [int(b) for _, b in data]

    print(part_1(A, B))
    print(part_2(A, B))
