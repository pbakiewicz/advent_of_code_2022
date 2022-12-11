with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()


def part_1() -> int:
    solution = 0
    for line in lines:
        first, second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")

        if int(first_start) == int(second_start):
            solution += 1
        elif int(first_start) > int(second_start):
            # first can only be included by second
            if int(first_end) <= int(second_end):
                solution +=1
        else:
            # second can only be included by first
            if int(first_end) >= int(second_end):
                solution+=1

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
