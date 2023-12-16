from math import sqrt, floor, ceil

def parseFile (path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def parseInput (_input: list) -> list:
    Durations = [int(durations) for durations in _input[0].split(": ")[1].split(" ") if durations]
    Length = [int(length) for length in _input[1].split(": ")[1].split(" ") if length]
    raceInfos = list(zip(Durations, Length))
    return(raceInfos)

def getPossibleWins (durations, length):
    rho = sqrt(durations**2 - 4*length)
    longestWait = (-durations - rho)/-2
    smallestWait = (-durations + rho)/-2

    if m.ceil (smallestWait) == smallestWait:
        smallestWait += 1
    if m.floor (longestWait) == longestWait:
        longestWait -= 1
    return(floor(longestWait) - ceil(smallestWait) + 1)


def main(_input: list, lettersNumber: bool=True) -> int:
    raceInfos = parseInput(_input)
    total = 0
    for info in raceInfos:
        number = getPossibleWins (*info)
        if total == 0:
            total += number
        else:
            total *= number
    return (total)

folder = "day6"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartOne:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
