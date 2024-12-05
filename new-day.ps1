$p = $args[0]
if ([int]$p -lt 10) {
    $p = "0$p"
}

New-Item -ItemType "directory" -Path "./$p" | Out-Null
New-Item -ItemType "file" -Path "./$p/input.txt" | Out-Null
New-Item -ItemType "file" -Path "./$p/sample.txt" | Out-Null
New-Item -ItemType "file" -Path "./$p/solution.py" | Out-Null

'def part_1(): ...


def part_2(): ...


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    print(part_1())
    print(part_2())
' | Add-Content -Path "./$p/solution.py"