def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def getWinningNumbers(_input:str) -> list:
    for index in range ( len (_input)):
        if _input[index] == ":":
            return (_input[index + 1:].strip().split())

def getCardWinners(elfNumbers, winningNumbers) -> int:
    count = 0
    for num in elfNumbers:
        if num in winningNumbers:
            count += 1
    return (count)

def main(_input: list, lettersNumber: bool=True) -> int:
    lineList = []
    amountSC = [1] * len(_input)
    for cardNumber in range(len(_input)):
        lineList = _input[cardNumber].split("|")
        winningNumbers = getWinningNumbers(lineList[0])
        elfNumbers =  lineList[1].strip().split()
        winingCount = getCardWinners(elfNumbers, winningNumbers)
        for index in range(winingCount):
            amountSC[cardNumber + index + 1] += amountSC[cardNumber]
    return (sum(amountSC))

folder = "day4"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile: list = parseFile(testPath)
configurationFile: list = parseFile(configurationPath)

# print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
