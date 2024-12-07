import re
from typing import Literal, TypeAlias

direction: TypeAlias = Literal["^", "v", "<", ">"]


def part_1(data: list[str]) -> int:
    m = data.copy()
    d: direction = "^"
    for i, l in enumerate(m):
        if d in l:
            pos = (i, l.index(d))
    try:
        while True:
            match d:
                case "^":
                    if m[pos[0] - 1][pos[1]] == "#":
                        d = ">"
                    else:
                        m[pos[0]] = m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                        pos = (pos[0] - 1, pos[1])
                case ">":
                    if m[pos[0]][pos[1] + 1] == "#":
                        d = "v"
                    else:
                        m[pos[0]] = m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                        pos = (pos[0], pos[1] + 1)
                case "v":
                    if m[pos[0] + 1][pos[1]] == "#":
                        d = "<"
                    else:
                        m[pos[0]] = m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                        pos = (pos[0] + 1, pos[1])
                case "<":
                    if m[pos[0]][pos[1] - 1] == "#":
                        d = "^"
                    else:
                        m[pos[0]] = m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                        pos = (pos[0], pos[1] - 1)
    except IndexError:
        pass
    p = sum(l.count("x") for l in m)
    return p + 1


def part_2(data: list[str]) -> int:
    def _inner(data: list[str]) -> bool:
        m = data.copy()
        d: direction = "^"
        moves = []
        recent = []
        pos = (0, 0)
        for i, l in enumerate(m):
            if d in l:
                pos = (i, l.index(d))
        try:
            while True:
                moves.append(pos)
                recent.append(pos)
                match d:
                    case "^":
                        if m[pos[0] - 1][pos[1]] == "#":
                            d = ">"
                            match = re.findall(
                                "("
                                + (
                                    "".join(map(str, recent))
                                    .replace("(", r"\(")
                                    .replace(")", r"\)")
                                    .replace(" ", "")
                                )
                                + ")",
                                "".join(map(str, moves)).replace(" ", ""),
                            )
                            if len(match) > 1:
                                break
                            recent.clear()
                        else:
                            m[pos[0]] = (
                                m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                            )
                            pos = (pos[0] - 1, pos[1])
                    case ">":
                        if m[pos[0]][pos[1] + 1] == "#":
                            d = "v"
                            match = re.findall(
                                "("
                                + (
                                    "".join(map(str, recent))
                                    .replace("(", r"\(")
                                    .replace(")", r"\)")
                                    .replace(" ", "")
                                )
                                + ")",
                                "".join(map(str, moves)).replace(" ", ""),
                            )
                            if len(match) > 1:
                                break
                            recent.clear()
                        else:
                            m[pos[0]] = (
                                m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                            )
                            pos = (pos[0], pos[1] + 1)
                    case "v":
                        if m[pos[0] + 1][pos[1]] == "#":
                            d = "<"
                            match = re.findall(
                                "("
                                + (
                                    "".join(map(str, recent))
                                    .replace("(", r"\(")
                                    .replace(")", r"\)")
                                    .replace(" ", "")
                                )
                                + ")",
                                "".join(map(str, moves)).replace(" ", ""),
                            )
                            if len(match) > 1:
                                break
                            recent.clear()
                        else:
                            m[pos[0]] = (
                                m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                            )
                            pos = (pos[0] + 1, pos[1])
                    case "<":
                        if m[pos[0]][pos[1] - 1] == "#":
                            d = "^"
                            match = re.findall(
                                "("
                                + (
                                    "".join(map(str, recent))
                                    .replace("(", r"\(")
                                    .replace(")", r"\)")
                                    .replace(" ", "")
                                )
                                + ")",
                                "".join(map(str, moves)).replace(" ", ""),
                            )
                            if len(match) > 1:
                                break
                            recent.clear()
                        else:
                            m[pos[0]] = (
                                m[pos[0]][: pos[1]] + "x" + m[pos[0]][pos[1] + 1 :]
                            )
                            pos = (pos[0], pos[1] - 1)
            return False
        except IndexError:
            return True

    m = data.copy()
    x = 0
    for i, l in enumerate(m):
        for j, v in enumerate(l):
            if v == ".":
                n = m.copy()
                n[i] = m[i][:j] + "#" + m[i][j + 1 :]
                if not _inner(n):
                    x += 1

    return x


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [l.strip() for l in f.readlines()]

    print(part_1(data))
    print(part_2(data))
