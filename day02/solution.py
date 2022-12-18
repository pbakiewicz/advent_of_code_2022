points = {
        "A": 1, # rock
        "B": 2, # paper
        "C": 3, # sicors
        "lost": 0,
        "draw": 3,
        "win": 6
    }

move = {
        "X": "lost",
        "Y": "draw",
        "Z": "win"
}

def get_action(op, my):
    result = move[my]
    if result == "lost":
        if op == "A":
            return "C"
        if op == "B":
            return "A"
        if op == "C":
            return "B"
    elif result == "draw":
        return op
    elif result == "win":
        if op == "A":
            return "B"
        if op == "B":
            return "C"
        if op == "C":
            return "A"


with open("puzzle.txt", "r") as puzzle:
    lines = puzzle.readlines()

moves = list()

for line in lines:
    op, my_move = line.strip().split(" ")
    moves.append((op, get_action(op, my_move)))


total_score = 0
for oponent, my in moves:
    total_score += points[my]
    if oponent == my:
        total_score += points["draw"]
    elif my == "A":
        total_score = total_score + (points["lost"] if oponent == "B" else points["win"])
    elif my == "B":
        total_score = total_score + (points["win"] if oponent == "A" else points["lost"])
    elif my == "C":
        total_score = total_score + (points["lost"] if oponent == "A" else points["win"])

print(total_score)
