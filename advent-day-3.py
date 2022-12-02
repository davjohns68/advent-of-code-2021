inputFile = open("/Users/djohnson/git/advent-of-code-2021/day3-input.txt", "r")
diagReport=[]
for item in inputFile:
    # Each line has "\n" appended to the end, so I'm stripping that to keeo the input clean
    diagReport.append(item.strip())

# PART 1
zeros = 0
ones = 0
gammaRate = ""
epsilonRate = ""
for bit in range(0,12):
    for line in diagReport:
        if line[bit] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gammaRate += "0"
        epsilonRate += "1"
    else:
        gammaRate += "1"
        epsilonRate += "0"
    zeros = 0
    ones = 0
print("Gamma Rate:", gammaRate, int(gammaRate, 2))
print("Epsilon Rate:", epsilonRate, int(epsilonRate, 2))
print("Power consumption:", int(gammaRate, 2) * int(epsilonRate, 2))

# PART 2
def mcv(bitPos, report):
    zeros = 0
    ones = 0
    for line in report:
        if line[bitPos] == "0":
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        return "1"
    else:
        return "0"

def lcv(bitPos, report):
    zeros = 0
    ones = 0
    for line in report:
        if line[bitPos] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros <= ones:
        return "0"
    else:
        return "1"

o2GeneratorRating = diagReport.copy()
tempList = []
while len(o2GeneratorRating) > 1:
    for bit in range(0,12):
        mostCommonValue = mcv(bit, o2GeneratorRating)
        for line in o2GeneratorRating:
            if line[bit] == mostCommonValue:
                tempList.append(line)
        o2GeneratorRating = tempList.copy()
        tempList = []
print(o2GeneratorRating)

co2ScrubberRating = diagReport.copy()
tempList = []
while len(co2ScrubberRating) > 1:
    for bit in range(0,12):
        leastCommonValue = lcv(bit, co2ScrubberRating)
        for line in co2ScrubberRating:
            if line[bit] == leastCommonValue:
                tempList.append(line)
        co2ScrubberRating = tempList.copy()
        tempList = []
        if len(co2ScrubberRating) < 2:
            break
print(co2ScrubberRating)

print("O2 Generator Rating:", o2GeneratorRating[0], int(o2GeneratorRating[0], 2))
print("CO2 Scrubber Rating:", co2ScrubberRating[0], int(co2ScrubberRating[0], 2))
print("Life Support Rating:", int(o2GeneratorRating[0], 2) * int(co2ScrubberRating[0], 2))
