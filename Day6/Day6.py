import time

def main():
    grid = Grid("Day6\input.txt")
    guard = Guard(grid.startingPosition)
    
    start = time.time()
    spacesToCheck = SolveMap(grid, guard)
    total = FindPotentialObstructions(grid, spacesToCheck)
    end = time.time()

    print("\nPotential Obstructions: " + str(total) + " in " + str(end - start) + " seconds")

def FindPotentialObstructions(grid, spacesToCheck):
    potentialObstructions = 0
    gridLength = len(grid.grid)

    count = 0
    for space in spacesToCheck:
        y = space[0]
        x = space[1]
        if grid.GetCharAtPosition(space) != ".":
            count += 1
            print("Option " + str(count) + " of " + str(gridLength) + " Skipped")
            continue

        start = time.time()

        grid.PlaceCharAtPosition("#", y, x)
        guard = Guard(grid.startingPosition)
        if CheckPlacement(grid, guard, y, x):
            potentialObstructions += 1
            print("Found potential obstruction, total is now: " + str(potentialObstructions))
        grid.PlaceCharAtPosition(".", y, x)
        count += 1
        print("Option " + str(count) + " of " + str(len(spacesToCheck)) + " Completed in " + str(time.time() - start) + " seconds", flush=True)

    return potentialObstructions

def CheckPlacement(grid, guard, y, x):
    spacesTravelled = [[guard.position.copy(), guard.forwardVector.copy()]]

    while True:
        if guard.GetNextPosition()[0] >= grid.gridLength or guard.GetNextPosition()[0] < 0:
            return False
        elif guard.GetNextPosition()[1] >= grid.gridLength or guard.GetNextPosition()[1] < 0:
            return False

        if grid.GetCharAtPosition(guard.GetNextPosition()) == "#":
            guard.TurnRight()
        elif grid.GetCharAtPosition(guard.GetNextPosition()) == ".":
            guard.Move()
        
        for position in spacesTravelled:
            if position == [guard.position, guard.forwardVector]:
                return True
        spacesTravelled.append([guard.position.copy(), guard.forwardVector.copy()])

def SolveMap(grid, guard):
    spacesTravelled = [guard.position.copy()]

    while True:
        if guard.GetNextPosition()[0] >= grid.gridLength or guard.GetNextPosition()[0] < 0:
            break
        elif guard.GetNextPosition()[1] >= grid.gridLength or guard.GetNextPosition()[1] < 0:
            break

        if grid.GetCharAtPosition(guard.GetNextPosition()) == "#":
            guard.TurnRight()
        elif grid.GetCharAtPosition(guard.GetNextPosition()) == ".":
            guard.Move()

        alreadyTravelled = False
        for position in spacesTravelled:
            if position == guard.position:
                alreadyTravelled = True
        if not alreadyTravelled: spacesTravelled.append(guard.position.copy())
    return spacesTravelled

class Guard:
    NORTH = [-1, 0]
    SOUTH = [1, 0]
    EAST = [0, 1]
    WEST = [0, -1]

    def __init__(self, position):
        self.position = [position[0], position[1]]
        self.forwardVector = Guard.NORTH
    
    def Move(self):
        self.position[0] += self.forwardVector[0]
        self.position[1] += self.forwardVector[1]
    
    def TurnRight(self):
        match self.forwardVector:
            case Guard.NORTH:
                self.forwardVector = Guard.EAST

            case Guard.EAST:
                self.forwardVector = Guard.SOUTH

            case Guard.SOUTH:
                self.forwardVector = Guard.WEST

            case Guard.WEST:
                self.forwardVector = Guard.NORTH


    def GetNextPosition(self):
        return [self.position[0] + self.forwardVector[0], self.position[1] + self.forwardVector[1]]

class Grid:
    def __init__(self, inputFileName):  
        self.grid = list()
        self.gridLength = 0
        self.startingPosition = [0, 0]

        newlineCounter = 0
        for i, char in enumerate(open(inputFileName).read()):
            match char:
                case "\n":
                    newlineCounter += 1
                    if self.gridLength == 0:
                        self.gridLength = i

                case "#":
                    self.grid.append(char)
                
                case ".":
                    self.grid.append(char)

                case "^":
                    self.startingPosition = self.IntToPosition(i - newlineCounter)
                    self.grid.append(".")

    def PrintGrid(self, guard):
        for y in range(self.gridLength):
            for x in range(self.gridLength):
                if guard.position == [y, x]:
                    print("X", end='')
                else: print(self.grid[(y * self.gridLength) + x], end='')
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
    main()