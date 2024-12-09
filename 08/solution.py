from itertools import product


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
            # when x0 >= x1
            #   x0 + dx
            #   x1 - dx
            # when x0 < x1
            #   x0 + (-dx)
            #   x1 - (-dx)
            xa = x0 + dx
            xb = x1 - dx

            # when y0 >= y1
            #   y0 + dy
            #   y1 - dy
            # when y0 < y1
            #   y0 + (-dy)
            #   y1 - (-dy)
            ya = y0 + dy
            yb = y1 - dy

            if 0 <= xa < len(data) and 0 <= ya < len(data[0]):
                A.add((xa, ya))
            if 0 <= xb < len(data) and 0 <= yb < len(data[0]):
                A.add((xb, yb))
    return len(A)


def part_2(data: list[str]) -> int:
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
            for i in range(len(data)):
                # when x0 >= x1
                #   x0 + dx * i
                #   x1 - dx * i
                # when x0 < x1
                #   x0 + (-dx * i)
                #   x1 - (-dx * i)
                xa = x0 + dx * i
                xb = x1 - dx * i

                # when y0 >= y1
                #   y0 + dy * i
                #   y1 - dy * i
                # when y0 < y1
                #   y0 + (-dy * i)
                #   y1 - (-dy * i)
                ya = y0 + dy * i
                yb = y1 - dy * i

                if 0 <= xa < len(data) and 0 <= ya < len(data[0]):
                    A.add((xa, ya))
                if 0 <= xb < len(data) and 0 <= yb < len(data[0]):
                    A.add((xb, yb))
    return len(A)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]

    print(part_1(data))
    print(part_2(data))
