def parseFile(path: str) -> list:
    with open(path) as file:
        return file.read().splitlines()


def countLetters(lettersCount: dict, string: str) -> None:
    for letter in string:
        if letter in lettersCount:
            lettersCount[letter] += 1
        else:
            lettersCount[letter] = 1


def getStrength(handDict: dict) -> int:
    handDictLen = len(handDict)
    valuesList:list = handDict.values()
    if not "J" in handDict:
        jokersNumber = 0
    else:
        jokersNumber = handDict["J"]
        handDict.pop("J")
    if jokersNumber and handDictLen != 1:
        handDictLen -= 1
    match handDictLen:
        case 1:
            return 7
        case 2:
            if max(valuesList) + jokersNumber == 4:
                return 6
            else:
                return 5
        case 3:
            if max(valuesList) + jokersNumber == 3:
                return 4
            else:
                return 3
        case 4:
            return 2
    return 1


def translateLine(hand: str) -> list:
    cards = list("aJ23456789TQKA")
    handList = [hand] * len(hand)
    for index in range(len(hand)):
        handList[index] = cards.index(hand[index])
    return handList2


def parseLine(line: str) -> tuple:
    hand, bid = line.split(" ")
    handDict = {}
    countLetters(handDict, hand)

    return (getStrength(handDict), translateLine(hand), bid)


def main(_input: list, lettersNumber: bool = True) -> int:
    tree = []
    total = 0
    for i in _input:
        tree.append(parseLine(i))
    tree.sort()

    for index, value in enumerate(tree):
        total += (index + 1) * int(value[2])
    return total


folder = "day7"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)
print("PartTwo:")
print("My testFile:\t\t", main(testFile))
print("My Puzzle input:\t", main(configurationFile))

