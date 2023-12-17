def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def main(_input: list, lettersNumber: bool=True) -> int:
    currArray = []
    sum = 0
    for line in _input:
        solutionArray = []
        solutionArray.append(list(map(int, line.split(" "))))
        currArray = solutionArray[0]

        while(not all(v == 0 for v in currArray)):
            temp = []
            for numberIndex, number in enumerate(currArray):
                if numberIndex < len(currArray) - 1:
                    temp.append(currArray[numberIndex + 1] - number)
            solutionArray.append(temp)
            currArray = solutionArray [-1]
        for index in range (-2, -len(solutionArray) - 1, -1):
            solutionArray[index].append(solutionArray[index][0] - solutionArray[index + 1][-1])
        sum += solutionArray[0][-1]
    return (sum)

folder = "day9"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
