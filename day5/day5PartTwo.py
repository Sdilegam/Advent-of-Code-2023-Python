def parseFile(path:str) -> str:
    with open(path) as file:
        return (file.read().splitlines())

def convert(locations: list, convertList: list):
    index = 0
    while index < len(locations):
        beginRange, endRange = locations[index]
        for conversion in convertList:
            destBegin, srcBegin, size = conversion
            if beginRange < srcBegin and srcBegin < endRange:
                tmp1, tmp2 = splitRange(locations[index], srcBegin)
                locations[index] = tmp1
                locations.append(tmp2)
                endRange = srcBegin
            elif beginRange < srcBegin + size and srcBegin + size < endRange:
                tmp1, tmp2 = splitRange(locations[index], srcBegin + size)
                locations[index] = tmp1
                locations.append(tmp2)
                endRange = srcBegin + size
            if srcBegin <= beginRange and srcBegin + size >= endRange:
                locations[index][0] += destBegin - srcBegin
                locations[index][1] += destBegin - srcBegin
                break
        index += 1


def splitRange(firstRange: list, intersection:int):
    return ([firstRange[0], intersection], [intersection, firstRange[1]])

def getSeeds(inputList: list):
    seedsRange = inputList[0][7:].split(" ")
    seeds = []
    for index in range (0, len(seedsRange), 2):
        seeds.append([int(seedsRange[index]), int(seedsRange[index]) + int(seedsRange[index + 1])])
    return (seeds)

def main(_input: list, lettersNumber: bool=True) -> int:
    locations = getSeeds(_input)
    convertList = []
    for index in range(3, len(_input)):
        if (not _input[index] or index == len(_input) - 1):
            convert(locations, convertList) 
            convertList.clear()
        if not _input[index] or not _input[index][0].isnumeric():
            continue
        convertList.append (list(map(int, _input[index].split(" "))))
    return (min(locations)[0])

folder = "day5"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

# print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
