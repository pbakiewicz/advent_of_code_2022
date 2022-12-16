from collections import defaultdict


with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()

def get_grid():
    grid = list()
    for line in lines:
        grid.append([int(c) for c in line.strip()])
    return grid


def part_1() -> int:
    grid = get_grid()
    total = 0
    for row, tree_list in enumerate(grid):
        for column, tree in enumerate(tree_list):
            if row == 0 or column == 0:
                total += 1
                continue
            elif column == len(tree_list) - 1:
                total += 1
                continue
            elif row == len(grid) -1:
                total += 1
                continue
            else:
                # from top
                for i in range(1, row +1):
                    if tree <= grid[row - i][column]:
                        break
                else:
                    total += 1
                    continue
                # from bottom
                for i in range(1, len(grid) - row):
                    if tree <= grid[row + i][column]:
                        break
                else:
                    total += 1
                    continue
                # from left
                for i in range(1, column +1):
                    if tree <= grid[row][column - i]:
                        break
                else:
                    total += 1
                    continue
                # from right
                for i in range(1, len(tree_list) - column):
                    if tree <= grid[row][column + i]:
                        break
                else:
                    total += 1
                    continue
    return total



def part_2() -> int:
    grid = get_grid()
    best = 0
    for row, tree_row in enumerate(grid):
        for column, tree in enumerate(tree_row):
            trees_up = row
            trees_down = len(grid) - row - 1
            trees_left = column
            trees_right = len(tree_row) - column - 1
            up, down, left, right = 0, 0, 0, 0
            for i in range(1, trees_up + 1):
                if grid[row - i][column] < tree:
                    up +=1
                else:
                    up += 1
                    break
            for i in range(1, trees_down + 1):
                if grid[row + i][column] < tree:
                    down +=1
                else:
                    down +=1
                    break
            for i in range(1, trees_left + 1):
                if grid[row][column -i] < tree:
                    left +=1
                else:
                    left +=1
                    break
            for i in range(1, trees_right + 1):
                if grid[row][column +  i] < tree:
                    right +=1
                else:
                    right +=1
                    break
            score = up * down * left * right
            if score > best:
                best = score
    return best

print(part_1())
print(part_2())
