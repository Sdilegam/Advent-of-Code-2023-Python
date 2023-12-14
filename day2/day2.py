def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().split("\n"))

def parseInput(inputString:list) -> list:
    outputList = [line.split(": ")[-1].strip().split("; ") for line in inputString if line]
    return (outputList)

def ispossible(inventory: {}, max: list) -> bool:
    return(inventory["red"] <= max[0] and inventory["green"] <= max[1] and inventory["blue"] <= max[2])

def main(inputString: str, part: int = 2) -> int:
    red, green, blue = 12, 13, 14
    inputList = parseInput(inputString)
    sum = 0
    for index, value in enumerate(inputList):
        if part == 2:
            totalCubes = {"red": 0, "blue": 0, "green": 0}
            red, green, blue = 0, 0, 0
        for draw in value:
            if part == 1:
                totalCubes = {"red": 0, "blue": 0, "green": 0}
                totalCubes["good"] = True
            splittedList = draw.split(", ")
            for colors in splittedList: 
                amount, color = colors.split(" ")
                if part == 1:
                    totalCubes[color] += int(amount)
                else:
                    totalCubes[color] = int(amount)
            if not ispossible(totalCubes, [red, green, blue]):
                if part == 1:
                    totalCubes["good"] = False
                    break
                else:
                    if totalCubes["red"] > red:
                        red = totalCubes["red"]
                    if totalCubes["green"] > green:
                        green = totalCubes["green"]
                    if totalCubes["blue"] > blue:
                        blue = totalCubes["blue"]
                    
        if part == 1:
            if totalCubes["good"] == True:
                sum += index + 1
        else:
            # print(totalCubes)
            sum += red * blue * green
            # print(red, green, blue, red * blue * green)
    return (sum)

import re


def max_cubes(line: str, comparison_color: str) -> int:
    cubes = re.findall(r'(\d+) (\w+)', line)
    return max(int(count) for count, color in cubes if color == comparison_color)

folder = "day2"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

print ("PartOne:")
print("testFile:\t", main(testFile, 1))
print("Puzzle input:\t", main(configurationFile, 1))

print ("\nPartTwo:")
print("testFile:\t", main(testFile))
print("Puzzle input:\t", main(configurationFile))
