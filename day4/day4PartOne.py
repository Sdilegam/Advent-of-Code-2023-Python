def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def getWinningNumbers(_input:str) -> list:
    for index in range ( len (_input)):
        if _input[index] == ":":
            return (_input[index + 1:].strip().split())

def getCardPoints(elfNumbers, winningNumbers) -> int:
    count = -1
    for num in elfNumbers:
        if num in winningNumbers:
            count += 1
    if count != -1:
        return (2**count)
    return (0)

def main(_input: list, lettersNumber: bool=True) -> int:
    sum = 0
    lineList = []
    for line in _input:
        lineList = line.split("|")
        winningNumbers = getWinningNumbers(lineList[0])
        elfNumbers =  lineList[1].strip().split()
        sum += getCardPoints(elfNumbers, winningNumbers)
    return (sum)

folder = "day4"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile: list = parseFile(testPath)
configurationFile: list = parseFile(configurationPath)

# print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
