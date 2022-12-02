inputFile = open("/Users/djohnson/git/advent-of-code-2021/day2-input.txt", "r")
moves=[]
for item in inputFile:
    # Each line has "\n" appended to the end, so I'm stripping that to keeo the input clean
    moves.append(item.strip())

# PART 1
horizontalPosition = 0
depth = 0
for move in moves:
    splitMove = move.split()
    if splitMove[0] == "forward":
        horizontalPosition += int(splitMove[1])
    elif splitMove[0] == "down":
        depth += int(splitMove[1])
    elif splitMove[0] == "up":
        depth -= int(splitMove[1])
print("Position hash:", horizontalPosition * depth)

# PART 2
horizontalPosition = 0
depth = 0
aim = 0
for move in moves:
    splitMove = move.split()
    if splitMove[0] == "forward":
        horizontalPosition += int(splitMove[1])
        depth += (aim * int(splitMove[1]))
    elif splitMove[0] == "down":
        aim += int(splitMove[1])
    elif splitMove[0] == "up":
        aim -= int(splitMove[1])
print("Part 2 position hash:", horizontalPosition * depth)