from itertools import permutations
from random import shuffle
from typing import Collection


def _check(
    page: Collection[int], _rules_before: dict[int, int], _rules_after: dict[int, int]
) -> bool:
    rules_before = _rules_before.copy()
    rules_after = _rules_after.copy()
    for p in page:
        if p in rules_after.values():
            b = [k for k, v in rules_after.items() if v == p]
            a = {
                k: (k if k in rules_before and rules_before[k] in page else 0)
                for k in b
            }
            if any(a.values()):
                return False
        if p in rules_before.values():
            b = [k for k, v in rules_before.items() if v == p]
            for k in b:
                rules_before.pop(k)
                rules_after.pop(k)
    return True


def part_1(rules: list[list[int]], pages: list[list[int]]) -> int:
    m = 0
    for page in pages:
        rules_before = {i: r[0] for i, r in enumerate(rules)}
        rules_after = {i: r[1] for i, r in enumerate(rules)}
        if _check(page, rules_before, rules_after):
            m += page[len(page) // 2]
    return m


def part_2(rules: list[list[int]], pages: list[list[int]]) -> int:
    m = 0
    for i, page in enumerate(pages):
        print(f"Working on {i}/{len(pages)}: {page}")
        rules_before = {i: r[0] for i, r in enumerate(rules)}
        rules_after = {i: r[1] for i, r in enumerate(rules)}
        if _check(page, rules_before, rules_after):
            continue
        for p in permutations(page):
            if _check(p, rules_before, rules_after):
                break
            else:
                page = list(p)
        m += page[len(page) // 2]
    return m


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
        data_r, data_p = data.split("\n\n")
        rules = [list(map(int, r.split("|"))) for r in data_r.split("\n")]
        pages = [list(map(int, p.split(","))) for p in data_p.split("\n")]

    print(part_1(rules, pages))
    print(part_2(rules, pages))
