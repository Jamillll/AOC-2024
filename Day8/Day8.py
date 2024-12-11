import sys

def main(argv):
    grid = Grid(argv[1])

    uniqueValues = list()
    for char in grid.grid:
        if char == ".":
            continue
        
        alreadyContains = False
        for value in uniqueValues:
            if char == value:
                alreadyContains = True
                break
        
        if not alreadyContains:
            uniqueValues.append(char)

    validHashtags = list()            
    for value in uniqueValues:
        valueFound = list()
        for y in range(grid.gridLength):
            for x in range(grid.gridLength):
                if grid.GetCharAtPosition([y, x]) == value:
                    valueFound.append([y, x])
        
        for location in valueFound:
            for otherLocations in valueFound:
                if location == otherLocations:
                    continue
                
                distance = [otherLocations[0] - location[0], otherLocations[1] - location[1]]
                if location[0] + (distance[0] * 2) < grid.gridLength and location[0] + (distance[0] * 2) >= 0:
                    if location[1] + (distance[1] * 2) < grid.gridLength and location[1] + (distance[1] * 2) >= 0:
                        validHashtags.append([location[0]+ (distance[0] * 2), location[1] + (distance[1] * 2)])
    
    for i, hashtag in enumerate(validHashtags):
        for j, otherHashtag in enumerate(validHashtags):
            if hashtag == otherHashtag and i != j:
                validHashtags.remove(otherHashtag)

    for y in range(grid.gridLength):
        for x in range(grid.gridLength):
            printedHashtag = False
            for hashtag in validHashtags:
                if hashtag == [y, x]:
                    print("#", end='')
                    printedHashtag = True
                    break
            if not printedHashtag:
                print(grid.GetCharAtPosition([y,x]), end="")
        print()

    print(len(validHashtags))

class Grid:
    def __init__(self, inputFileName):  
        self.grid = list()
        self.gridLength = 0

        newlineCounter = 0
        for i, char in enumerate(open(inputFileName).read()):
            match char:
                case "\n":
                    newlineCounter += 1
                    if self.gridLength == 0:
                        self.gridLength = i
                
                case ".":
                    self.grid.append(char)

                case _:
                    self.grid.append(char)

    def PrintGrid(self):
        for y in range(self.gridLength):
            for x in range(self.gridLength):
                print(self.grid[(y * self.gridLength) + x], end='')
            print()

    def PrintPosition(self, y, x):
        print(self.grid[(y * self.gridLength) + x])
    
    def IntToPosition(self, number):
        for i in range(self.gridLength):
            if number >= i * self.gridLength and number < (i + 1) * self.gridLength:
                return [i, number - (i * self.gridLength)]

    def PlaceCharAtPosition(self, charToPlace, y, x):
        self.grid[(y * self.gridLength) + x] = charToPlace

    def GetCharAtPosition(self, position):
        return self.grid[(position[0] * self.gridLength) + position[1]]

if __name__ == "__main__":
    main(sys.argv)