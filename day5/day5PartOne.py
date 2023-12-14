def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def convert(locations: list, convertList: list):
    for index in range(len(locations)):
        for conversion in convertList:
            destBegin, srcBegin, size = conversion
            if srcBegin <= locations[index] and locations[index] < srcBegin + size:
                locations[index] = locations[index] - srcBegin + destBegin
                break

def main(_input: list, lettersNumber: bool=True) -> int:
    locations = list(map(int, _input[0][7:].split(" ")))
    convertList = []
    for index in range(3, len(_input)):
        if (not _input[index] or index == len(_input) - 1):
            convert(locations, convertList)
            convertList.clear()
        if not _input[index] or not _input[index][0].isnumeric():
            continue
        convertList.append (list(map(int, _input[index].split(" "))))
    return (min(locations))

folder = "day5"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

# print(testFile)

print ("PartOne:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
