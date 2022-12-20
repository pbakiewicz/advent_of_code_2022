with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()

def get_cycles():
    # number of during cycle: X
    cycle = 0
    cycles = {cycle: 1}
    for instruction in [line.strip() for line in lines]:
        if instruction == "noop":
            cycle += 1
            cycles[cycle] = cycles[cycle - 1]
        else:
            _, addon = instruction.split()
            addon = int(addon)
            cycle += 1
            cycles[cycle] = cycles[cycle - 1] 
            cycle += 1
            cycles[cycle] = cycles[cycle - 1]  + addon

    return cycles


def part_1() -> int:
    cycles = get_cycles()
    result = 0
    for c in [20, 60, 100, 140, 180, 220]:
        result += cycles[c -1] * c
    return result


def part_2():
    cycles = get_cycles()
    screen = list()
    for beam in range(40 * 6):
        sprite = cycles[beam]
        beam = beam % 40
        if beam in range(sprite - 1, sprite +2):
            screen.append("#")
        else:
            screen.append(".")

    for row in range(6):
        print("".join(screen[row * 40:(row+1) * 40]))



print(part_1())
part_2()
