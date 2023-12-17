from math import lcm

def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def inputToDict(_input: list) -> dict:
    nodeDict = {}
    startNodes = []
    for line in _input:
        node, next = line.split(" = ")
        next = next.strip("()").split(", ")
        next = tuple(next)
        nodeDict[node] = next
        if node[-1] == "A":
            startNodes.append(node)
    return (nodeDict, startNodes)

def allOnZ(nodes: list) -> bool:
    for node in nodes:
        if node[-1] != "Z":
            return (False)
    return (True)

def main(_input: list, lettersNumber: bool=True) -> int:
    with open("log.txt", "w") as file_:
        moves = _input[0]
        nodeDict, currNodes = inputToDict (_input[2: len (_input)])
        lenMoves = len(_input[0])
        steps = 0
        stepsNeeded = len(currNodes) * [-1]
        while(-1 in stepsNeeded):
            index = steps % lenMoves
            for nodeIndex in range ( len (currNodes)):
                nodeVal = currNodes[nodeIndex]
                if moves[index] == "L":
                    currNodes[nodeIndex] = nodeDict[nodeVal][0]
                else:
                    currNodes[nodeIndex] = nodeDict[nodeVal][1]
                if stepsNeeded[nodeIndex] == -1 and currNodes[nodeIndex][-1] == "Z":
                    stepsNeeded[nodeIndex] = steps + 1
            steps += 1
        return (lcm(*stepsNeeded))

folder = "day8"
testPath = f"{folder}/{folder}Test1.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
