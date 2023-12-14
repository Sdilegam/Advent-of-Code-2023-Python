def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def main(_input: list, lettersNumber: bool=True) -> int:

    return ()

folder = "day"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
# configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartOne:")
print("testFile:\t", main(testFile))
# print("Puzzle input:\t", main(configurationFile))
