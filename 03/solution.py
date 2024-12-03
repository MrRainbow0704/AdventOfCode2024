import re


def part_1(s: str) -> int:
    m = re.findall(r"mul\((\d+),(\d+)\)", s)
    x = 0
    for a, b in m:
        x += int(a) * int(b)
    return x


def part_2(s: str) -> int:
    m = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", s)
    x, enabled = 0, True
    for a, b, do, dont in m:
        if a != "" and b != "" and enabled:
            x += int(a) * int(b)
        elif do != "":
            enabled = True
        elif dont != "":
            enabled = False
    return x


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
