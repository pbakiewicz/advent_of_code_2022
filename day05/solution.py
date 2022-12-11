from collections import defaultdict
import re

with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.read()
    first_half, second_half = lines.split("\n\n")

def get_stacks() -> dict:
    all_stacks = defaultdict(list)
    
    for line in first_half.split("\n")[:-1]:
        for i, crate_symbol in enumerate(line[1::4]):
            if not crate_symbol.isspace():
                all_stacks[i + 1].append(crate_symbol)

    for crates in all_stacks.values():
        crates.reverse()

    return all_stacks

def get_moves() -> list:
    moves = list()

    for line in second_half.split("\n"):
        if line:
            pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
            quantity, f, t = re.search(pattern,line).groups() 
            moves.append((int(quantity), int(f), int(t)))
    return moves

def part_1() -> str:
    all_stacks = get_stacks() 
    moves = get_moves()
    for quantity, f, t in moves:
        for _ in range(quantity):
            crate = all_stacks[f].pop()
            all_stacks[t].append(crate)

    result = ""
    for stack_no in range(10):
        try:
            result += all_stacks[stack_no].pop()
        except IndexError:
            pass
    return result

def part_2() -> str:
    all_stacks = get_stacks() 
    moves = get_moves()
    for quantity, f, t in moves:
        crate_set = all_stacks[f][-quantity:]
        all_stacks[t] += crate_set
        del all_stacks[f][-quantity:]

    result = ""
    for stack_no in range(10):
        try:
            result += all_stacks[stack_no].pop()
        except IndexError:
            pass
    return result

print("Part 1 =", part_1())
print("Part 2 =", part_2())
