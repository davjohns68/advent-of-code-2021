inputFile = open("/Users/djohnson/git/advent-of-code-2021/day4-input.txt", "r")
bingoGame=[]
for item in inputFile:
    # Each line has "\n" appended to the end, so I'm stripping that to keeo the input clean
    bingoGame.append(item.strip())

# Process boards
numberDraws = bingoGame[0].split(',')
print(bingoGame[-1])

# PART 1
