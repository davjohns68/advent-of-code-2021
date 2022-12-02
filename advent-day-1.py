inputFile = open("/Users/djohnson/git/advent-of-code-2021/day1-input.txt", "r")
depths=[]
for item in inputFile:
    depths.append(int(item))

# PART 1
totalDepthIncreases = 0
for i in range(0,len(depths) - 1):
    if depths[i + 1] > depths[i]:
        totalDepthIncreases += 1

print("Total depth increases:", totalDepthIncreases)

# PART 2
currWindow = depths[0] + depths[1] + depths[2]
nextWindow = 0
totalWindowIncreases = 0
for i in range(1,len(depths) - 2):
    if i + 2 <= len(depths):
        nextWindow = depths[i] + depths[i + 1] + depths[i + 2]
        if nextWindow > currWindow:
            totalWindowIncreases += 1
        currWindow = nextWindow

print("Total window increases:", totalWindowIncreases)