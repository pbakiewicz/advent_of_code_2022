from collections import defaultdict
import re

with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.read()

def part_1() -> int:
    input = iter(lines)
    letter_no = 4
    marker = [next(input), next(input), next(input), next(input)]
    while True:
        if len(set(marker)) == 4:
            return letter_no
        else:
            del marker[0]
            marker.append(next(input))
            letter_no += 1


def part_2() -> int:
    input = iter(lines)
    letter_no = 14
    marker = [next(input) for _ in range(14)]
    print(marker)
    while True:
        if len(set(marker)) == 14:
            return letter_no
        else:
            del marker[0]
            marker.append(next(input))
            letter_no += 1

print("Part 1 =", part_1())
print("Part 2 =", part_2())
