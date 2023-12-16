

def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def countLetters(lettersCount: dict, string: str)-> None:
    for letter in string:
        if letter in lettersCount:
            lettersCount [letter] += 1
        else:
            lettersCount[letter] = 1


def getStrength(handDict:dict)->int:
    handDictLen = len(handDict)
    valuesList = handDict.values()
    match handDictLen:
        case 1:
            return (7)
        case 2:
            if 4 in valuesList:
                return (6)
            else:
                return (5)
        case 3:
            if 3 in valuesList:
                return (4)
            else:
                return (3)
        case 4:
            return (2)
    return(1)

def parseLine(line:str) -> tuple:
    hand, bid = line.split(" ")
    handDict = {}
    countLetters(handDict, hand)
    return (hand, bid, getStrength(handDict))

def isStronger(first: tuple, second: tuple) -> bool:
    if first == None:
        return (False)
    if second == None:
        return (True)
    firstStrength = first[2]
    firstHand = first[0]
    secondStrength = second[2]
    secondHand = second[0]
    cards = list("23456789TJQKA")
    if firstStrength > secondStrength:
        return (True)
    if firstStrength < secondStrength:
        return (False)
    for index in range(len(firstHand)):
        firstHandLetter = firstHand[index]
        secondHandLetter = secondHand[index]
        if cards.index(firstHandLetter) > cards.index(secondHandLetter):
            return (True)
        if cards.index(firstHandLetter) < cards.index(secondHandLetter):
            return (False)

def heapify(handsHeap, index):
    if index >= (len(handsHeap)//2) and index <= len(handsHeap):
        return
    leftChild = None
    rightChild = None
    leftIndex = 2*index + 1
    rightIndex = 2*index + 2
    if (leftIndex < len(handsHeap)):
        leftChild = handsHeap[leftIndex]
    if (rightIndex < len(handsHeap)):
        rightChild = handsHeap[rightIndex]
    current = handsHeap[index]
    temp = ()
    if leftChild == None and rightChild == None:
        return
    if isStronger(leftChild, current) or isStronger(rightChild, current,):
        if isStronger(leftChild, rightChild):
            handsHeap[leftIndex], handsHeap[index] = handsHeap[index], handsHeap[leftIndex]
            heapify(handsHeap, leftIndex)
        else:
            handsHeap[rightIndex], handsHeap[index] = handsHeap[index], handsHeap[rightIndex]
            heapify(handsHeap, rightIndex)

def addHeap(handsHeap: list, toAdd: tuple):
    index = len(handsHeap)
    parentIndex = (index - 1)//2
    handsHeap.append(toAdd)
    while index > 0 and isStronger(handsHeap[index], handsHeap[parentIndex]):
        handsHeap[index], handsHeap[parentIndex] =  handsHeap[parentIndex], handsHeap[index]
        index = parentIndex
        parentIndex = (index - 1)//2

def popHead(handsHeap: list):
    if len(handsHeap) != 0:
        head = handsHeap[0]
    temp = handsHeap.pop()
    if (handsHeap.__len__() >= 1):
        handsHeap[0] = temp
        heapify(handsHeap, 0)
    return (head)

def main(_input: list, lettersNumber: bool=True) -> int:
    tree = []
    total = 0
    for i in _input:
        addHeap(tree, parseLine(i))
    for i in range(len(tree), 0, -1):
        winning = int(popHead(tree)[1])
        rank = i
        mult = winning * rank
        total += mult
    return (total)

folder = "day7"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartOne:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
