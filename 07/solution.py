from pprint import pp
import re


def part_1(data: list[str]) -> int:
    d = [list(map(int, re.match(r"(\d+): (\d+) (\d+)", l).groups())) for l in data]  # type: ignore
    for l in d:
        r = d[0]
        vals = d[1:]

        
    return 0


def part_2(): ...


if __name__ == "__main__":
    with open("sample.txt") as f:
        data = f.readlines()

    print(part_1(data))
    print(part_2())
