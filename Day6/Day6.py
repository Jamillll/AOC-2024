def main():
    grid = Grid("Day6\input.txt")
    guard = Guard(grid.startingPosition)
    
    spacesTravelled = [guard.position.copy()]
    while True:
        if guard.GetNextPosition()[0] >= grid.gridLength or guard.GetNextPosition()[0] < 0:
            break
        elif guard.GetNextPosition()[1] >= grid.gridLength or guard.GetNextPosition()[1] < 0:
            break

        if grid.GetCharAtPositon(guard.GetNextPosition()) == "#":
            guard.TurnRight()
        elif grid.GetCharAtPositon(guard.GetNextPosition()) == ".":
            guard.Move()

            alreadyTravelled = False
            for position in spacesTravelled:
                if position == guard.position:
                    alreadyTravelled = True
            if not alreadyTravelled: spacesTravelled.append(guard.position.copy())
    print("Spaces Travelled: " + str(len(spacesTravelled)))

        

class Guard:
    def __init__(self, position):
        self.position = [position[0], position[1]]
        self.forwardVector = [-1, 0]
    
    def Move(self):
        self.position[0] += self.forwardVector[0]
        self.position[1] += self.forwardVector[1]
    
    def TurnRight(self):
        match self.forwardVector:
            case [-1,0]:
                self.forwardVector = [0,1]

            case [0,1]:
                self.forwardVector = [1,0]

            case [1,0]:
                self.forwardVector = [0,-1]

            case [0,-1]:
                self.forwardVector = [-1,0]


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
        
    def GetCharAtPositon(self, position):
        return self.grid[(position[0] * self.gridLength) + position[1]]

if __name__ == "__main__":
    main()