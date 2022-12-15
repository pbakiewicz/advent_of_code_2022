import os

with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()


def get_filesystem():
    current_folder = "/"
    files = dict()
    dirs = dict()
    for line in lines[1:]:
        if line.startswith("$ cd"):
            folder = line.split()[-1]
            current_folder = os.path.abspath(os.path.join(current_folder, folder))
            dirs[current_folder] = 0
        elif not line.startswith("$") and not line.startswith("dir"):
            size, filename = line.split()
            file = os.path.join(current_folder, filename)
            files[file] = int(size)

    for dir in dirs:
        for file in files:
            if file.startswith(dir):
                dirs[dir] += files[file]

    return files, dirs

def part_1() -> int:
    max = 100000
    _, dirs = get_filesystem()
    total = 0
    for _, size in dirs.items():
        if size <= max:
            total += size
    return total

def part_2() -> int:
    _, dirs = get_filesystem()
    avail = 70000000
    needs = 30000000
    to_be_deleted = needs - (avail - dirs["/"] )
    closest = dirs["/"]
    for size in dirs.values():
        candidate_size = size - to_be_deleted
        if candidate_size >= 0: 
            if candidate_size < (closest - to_be_deleted):
                closest = size
    return closest

print(part_1())
print(part_2())
