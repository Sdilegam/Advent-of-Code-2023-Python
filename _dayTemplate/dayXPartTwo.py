def parseFile(path:str) -> str:
    with open(path) as file:
        return (file.read().splitlines())

def main(_input: str, lettersNumber: bool=True) -> int:

    return ()

folder = "day"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
# configurationFile = parseFile(configurationPath)

print(testFile)

print ("PartTwo:")
print("testFile:\t", main(testFile))
# print("Puzzle input:\t", main(configurationFile))
