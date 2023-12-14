def parseFile(path:str) -> str:
    with open(path) as file:
        return (file.read().splitlines())

def parseInput (_input: list) -> list:
    Durations = _input[0].split(": ")[1].replace(" ", "")
    Length = _input[1].split(": ")[1].replace(" ", "")
    raceInfos = (int(Durations), int(Length))
    print (raceInfos)
    return(raceInfos)

def getPossibleWins (Durations, Length):
    shortestWait = 0
    longestWait = 0
    for time in range (Durations - 1, 0, -1):
        speed = time
        traveledLength = (Durations - time) * speed
        if traveledLength > Length:
            longestWait = time
            break
    for time in range (1, longestWait):
        speed = time
        traveledLength = (Durations - time) * speed
        if traveledLength > Length:
            shortestWait = time
            break
    return(longestWait - shortestWait + 1)


def main(_input: list, lettersNumber: bool=True) -> int:
    raceInfos = parseInput(_input)
    total = 0
    total = getPossibleWins(*raceInfos)
    return (total)

folder = "day6"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
