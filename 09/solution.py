def part_1(data: str) -> int:
    file = data[0::2]
    free = data[1::2] + "0"

    s = "".join(
        int(fl) * chr(i + 100) + int(fr) * "."
        for i, (fl, fr) in enumerate(zip(file, free))
    )

    ss = s
    for c in s[::-1]:
        ss = ss[::-1].replace(c, ".", 1)[::-1].replace(".", c, 1)

    x = 0
    for i, c in enumerate(ss):
        if c == ".":
            c = chr(0 + 100)
        x += i * (ord(c) - 100)
    return x


def part_2(data: str) -> int:
    file = data[0::2]
    free = data[1::2] + "0"

    s = "".join(
        int(fl) * chr(i + 100) + int(fr) * "."
        for i, (fl, fr) in enumerate(zip(file, free))
    )

    ss = s
    moved = set()
    for i, c in enumerate(s[::-1]):
        if c in moved or c == ".":
            continue
        q = s.count(c)
        moved.add(c)
        if ss.count("." * q):
            ss = ss[::-1].replace(c * q, "." * q, 1)[::-1].replace("." * q, c * q, 1)

    x = 0
    for i, c in enumerate(ss):
        if c == ".":
            c = chr(0 + 100)
        x += i * (ord(c) - 100)
    return x


if __name__ == "__main__":
    with open("sample.txt") as f:
        data = f.read()

    print(part_1(data))
    print(part_2(data))
