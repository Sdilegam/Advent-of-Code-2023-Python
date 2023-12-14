def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def computeCoord(coord, maxLen) -> int:
    if coord < 0:
        return(0)
    if coord > maxLen:
        return (maxLen)
    return (coord)

def checkSymbol(array:list, arrayLen: int, xCoords: tuple, yCoord: int, gearsPos: dict) -> bool:
    for yIndex in range (computeCoord(yCoord - 1, len(array)), computeCoord(yCoord + 2, len(array))):
        for xIndex in range (computeCoord(xCoords[0] - 1, arrayLen), computeCoord(xCoords[1] + 1, arrayLen)):
            if yIndex == yCoord and (xCoords[0] <= xIndex and xIndex < xCoords[1]):
                continue
            if array[yIndex][xIndex] == "*":
                key = (yIndex, xIndex)
                value = int(array[yCoord][xCoords[0]:xCoords[1]])
                if key not in gearsPos:
                    gearsPos[key] = [value]
                else:
                    gearsPos[key].append(value)
    return False

def getAllGears(array: list) -> list:
    arrayLen = len(array[0])
    gears = {}
    for yCoord, line in enumerate(array):
        beginIndex, endIndex = 0, 0
        while beginIndex < arrayLen:
            if not line[beginIndex].isnumeric():
                endIndex += 1
                beginIndex += 1
            elif endIndex < arrayLen and line[endIndex].isnumeric():
                endIndex += 1
            elif beginIndex == endIndex:
                endIndex += 1
            else:
                checkSymbol(array, arrayLen, (beginIndex, endIndex), yCoord, gears)
                beginIndex = endIndex
    return (gears)


def main(array: list) -> int:
    total = 0
    allGears = getAllGears(array)
    for gear in allGears.values():
        if len (gear) == 2:
            total += gear[0] * gear[1]
    return (total)

folder = "day3"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartOne:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))

