with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()


def part_1() -> int:
    solution = 0
    for line in lines:
        half = len(line)//2
        first_half = line[:half]
        second_half = line[half:]
        char_set = set(first_half) & set(second_half)
        char = char_set.pop()
        upper = char.isupper()
        if upper:
            points = 27 + ord(char) - ord('A')
        else:
            points = 1 + ord(char) - ord('a')
        solution += points

    return solution

def part_2() -> int:
    solution = 0
    groups = len(lines) // 3
    for group_no in range(groups):
        group_lines = lines[group_no * 3: (group_no+1) *3]
        for char in group_lines[0]:
            if char in group_lines[1] and char in group_lines[2]:
                upper = char.isupper()
                points = ord(char) - (38 if upper else 96)
                solution += points
                break
    return solution

