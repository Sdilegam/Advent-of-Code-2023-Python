def main(_input: list, lettersNumber: bool=True) -> int:
    lineNumbers = []
    parsedArray = []
    numbersList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    sum = 0

    parsedArray = [line for line in _input if line]
    # print(parsedArray)
    for line in parsedArray:
        lineNumbers = []
        index = 0
        while (index < len (line)):
            char = line[index]
            if char.isnumeric():
                lineNumbers.append(char)
            elif lettersNumber:
                for indexNumber, number in enumerate(numbersList):
                    if line[index : index + len(number)] == number:
                        lineNumbers.append(str(indexNumber + 1))
                        break
            index += 1
        if lineNumbers:
            sum += int(lineNumbers[0] + lineNumbers[-1])
    return (sum)

def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

folder = "day1"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print ("PartOne:")
print("testFile:\t", main(testFile, False))
print("Puzzle input:\t", main(configurationFile, False))

print ("\nPartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
