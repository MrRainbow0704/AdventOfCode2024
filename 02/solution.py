from itertools import repeat


def _increasing(r: list[int]) -> bool:
    return all(map(lambda v: True if v[0] < v[1] else False, zip(r, r[1:])))


def _decreasing(r: list[int]) -> bool:
    return all(map(lambda v: True if v[0] > v[1] else False, zip(r, r[1:])))


def _delta(r: list[int]) -> bool:
    return all(
        map(
            lambda v: True if 1 <= abs(v[1] - v[0]) <= 3 else False,
            zip(r, r[1:]),
        )
    )


def part_1(reports: list[list[int]]) -> int:
    s = 0
    for report in reports:
        if (_increasing(report) or _decreasing(report)) and _delta(report):
            s += 1
    return s


def part_2(reports: list[list[int]]) -> int:
    s = 0
    for report in reports:
        if (_increasing(report) or _decreasing(report)) and _delta(report):
            s += 1
        else:
            for i, test in enumerate(repeat(report, len(report))):
                t = test.copy()
                t.pop(i)

                if (_increasing(t) or _decreasing(t)) and _delta(t):
                    s += 1
                    break
    return s


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [list(map(int, x.split())) for x in f.readlines()]

    print(part_1(data))
    print(part_2(data))
