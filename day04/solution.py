with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()


def part_1() -> int:
    solution = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = int(second_start), int(second_end)

        if first_start <= second_start <= second_end <= first_end:
            solution += 1
        elif second_start <= first_start <= first_end <= second_end:
            solution += 1

    return solution


def part_2() -> int:
    solution = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end = int(first_start), int(first_end)
        second_start, second_end = int(second_start), int(second_end)

        if not ((first_end < second_start) or (second_end < first_start)):
            solution += 1


    return solution

print("Part 1 =", part_1())
print("Part 2 =", part_2())
