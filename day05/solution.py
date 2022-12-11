from collections import defaultdict
import re

with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()

def get_stacks() -> dict:
    all_stacks = defaultdict(list)
    stack_no = 9
    
    for line in lines[:8]:
        for i in range(stack_no):
            crate_symbol = line[1 + i *4]
            if crate_symbol.strip():
                all_stacks[i + 1].append(crate_symbol)

    for crates in all_stacks.values():
        crates.reverse()

    return all_stacks

def get_moves() -> list:
    moves = list()

    for line in lines[10:]:
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
        all_stacks[f] = all_stacks[f][:-quantity]

    result = ""
    for stack_no in range(10):
        try:
            result += all_stacks[stack_no].pop()
        except IndexError:
            pass
    return result

print("Part 1 =", part_1())
print("Part 2 =", part_2())
