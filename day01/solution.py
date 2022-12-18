from collections import defaultdict


def main():
    with open("/home/pawel//advent_of_code/2022/1/input.txt", "r") as input_file:
        elves = get_elves(input_file.readlines())

        total_calories = 0
        for _ in range(3):
            max_elf = get_max_calories(elves)
            calories = elves[max_elf]
            print("current_max elf=", max_elf, " curring calories = ", calories)
            total_calories += calories
            del elves[max_elf]

        print("TOTAL CALORIES= ", total_calories) 


def get_elves(raw_input: list) -> dict:
    elves = defaultdict(int)
    elf_no = 1
    for line in raw_input:
        if value := line.strip():
            elves[elf_no] += int(value)
        else:
            elf_no += 1
    return elves

def get_max_calories(elves: dict) -> int:
    max_elf = None
    for elf_no, calories in elves.items():
        if not max_elf:
            max_elf = elf_no
        else:
            if calories > elves[max_elf]:
                max_elf = elf_no

    return max_elf





main()
