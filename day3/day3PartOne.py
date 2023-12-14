def parseFile(path:str) -> list:
    with open(path) as file:
        return (file.read().splitlines())

def computeCoord(coord, maxLen) -> int:
    if coord < 0:
        return(0)
    if coord > maxLen:
        return (maxLen)
    return (coord)

def checkSymbol(array:list, arrayLen: int, xCoords: tuple, yCoord: int) -> bool:
    for yIndex in range (computeCoord(yCoord - 1, len(array)), computeCoord(yCoord + 2, len(array))):
        for xIndex in range (computeCoord(xCoords[0] - 1, arrayLen), computeCoord(xCoords[1] + 1, arrayLen)):
            if yIndex == yCoord and (xCoords[0] <= xIndex and xIndex < xCoords[1]):
                continue
            if not array[yIndex][xIndex].isnumeric() and not array[yIndex][xIndex] == ".":
                return (True)
    return False

def getValidNumbers(array: list) -> list:
    arrayLen = len(array[0])
    numbers = []
    for yCoord, line in enumerate(array):
        beginIndex, endIndex = 0, 0
        while beginIndex < arrayLen:
            if not line[beginIndex].isnumeric():
                endIndex += 1
                beginIndex += 1
            elif endIndex < arrayLen and line[endIndex].isnumeric():
                endIndex += 1
            elif beginIndex == endIndex:
                endIndex += 1
            else:
                if checkSymbol(array, arrayLen, (beginIndex, endIndex), yCoord):
                    numbers.append(int(line[beginIndex:endIndex]))
                beginIndex = endIndex
    return (numbers)


def main(array: list) -> int:
    validNumbers = getValidNumbers(array)
    sumOfNumbers = sum(validNumbers)
    return (sumOfNumbers)

folder = "day3"
testPath = f"{folder}/{folder}Test.txt"
configurationPath = f"{folder}/{folder}Input.txt"

testFile = parseFile(testPath)
configurationFile = parseFile(configurationPath)

def checkenv(start_x,start_y,nbr,string):
    positions = []
    
    for i in range(start_y-1,start_y+len(nbr)+1,1):
        for j in range(start_x-1,start_x+2,1):
            legal = True
            if i < 0 or j < 0:
                legal = False
            if i >= len(string[0]) or j >= len(string):

                legal = False
            for k in range(len(nbr)):
                if i == start_x + k and j == start_y :
                    legal = False
            if legal == True:
                positions.append([i,j])
            
    output = 0

    for i in range(len(positions)):
        #print(positions[i][1],positions[i][0])
        if string[positions[i][1]][positions[i][0]] != "." and string[positions[i][1]][positions[i][0]].isnumeric() == False :
            output = int(nbr)
    
    return output
            
            
string = configurationFile

#string = [element for element in string if element != '']
print(string)
info = []
for i in range(len(string)):
    tmp = - 1
    for j in range(len(string[i])): 
        if string[i][j].isnumeric() == True and j > tmp:
            incr = 0
            nbr = ""
            while j+incr != len(string[i]) and string[i][j+incr].isnumeric() == True:
                nbr += string[i][j+incr]
                incr += 1
                
            info.append([i,j,nbr])
            tmp = j + len(nbr)
result = 0            
for i in range(len(info)):
    result += checkenv(info[i][0],info[i][1],info[i][2],string)

print(result)



# print ("PartOne:")
# print("testFile:\t", main(testFile))
# print("Puzzle input:\t", main(configurationFile))
