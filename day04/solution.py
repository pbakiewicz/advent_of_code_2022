with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()


def part_1() -> int:
    solution = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_section = set(range(int(first_start), int(first_end) + 1))
        second_section = set(range(int(second_start), int(second_end) + 1))
        if first_section == second_section:
            solution += 1
        elif first_section.issubset(second_section):
            solution += 1
        elif second_section.issubset(first_section):
            solution += 1

    return solution

def part_2() -> int:
    solution = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")

        first_section = range(int(first_start), int(first_end) +1)
        second_section = range(int(second_start), int(second_end) +1)

        if set(first_section) & set(second_section):
            solution += 1

    return solution

print("Part 1 =", part_1())
print("Part 2 =", part_2())
