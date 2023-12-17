def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def inputToDict(_input: list) -> dict:
    nodeDict = {}
    for line in _input:
        node, next = line.split(" = ")
        next = next.strip("()").split(", ")
        next = tuple(next)
        nodeDict[node] = next
    return (nodeDict)

def main(_input: list, lettersNumber: bool=True) -> int:
    moves = _input[0]
    currNode = "AAA"
    nodeDict = inputToDict (_input[2: len (_input)])
    lenMoves = len(_input[0])
    steps = 0
    test = 0
    while(currNode != "ZZZ"):
        index = steps % lenMoves
        if moves[index] == "L":
            currNode = nodeDict[currNode][0]
        else:
            currNode = nodeDict[currNode][1]
        steps += 1
        # print(steps)
    return (steps)

folder = "day8"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartOne:")
# print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
