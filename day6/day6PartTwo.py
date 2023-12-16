from math import sqrt, floor, ceil

def parseFile(path:str) -> str:
    with open(path) as file:
        return (file.read().splitlines())

def parseInput (_input: list) -> list:
    Durations = _input[0].split(": ")[1].replace(" ", "")
    Length = _input[1].split(": ")[1].replace(" ", "")
    raceInfos = (int(Durations), int(Length))
    print (raceInfos)
    return(raceInfos)

def getPossibleWins (durations, length):
    rho = sqrt(durations**2 - 4*length)
    longestWait = (-durations - rho)/-2
    smallestWait = (-durations + rho)/-2

    if ceil (smallestWait) == smallestWait:
        smallestWait += 1
    if floor (longestWait) == longestWait:
        longestWait -= 1
    return(floor(longestWait) - ceil(smallestWait) + 1)


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
