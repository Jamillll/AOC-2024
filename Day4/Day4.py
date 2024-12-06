def SearchForWord(grid, searchWord, targetX, targetY):
    total = 0
    if targetX >= len(grid[0]) or targetY >= len(grid):
        return 0
    
    vectorsToCheck = list()
    for y in range(max(targetY - 1, 0), min(targetY + 2, len(grid))):
        for x in range(max(targetX - 1, 0), min(targetX + 2, len(grid[0]))):
            if x == targetX and y == targetY:
                continue
            if grid[y][x] == searchWord[1]:
                vectorsToCheck.append((y - targetY, x - targetX))
    
    for vector in vectorsToCheck:
        foundWord = False
        for i, letter in enumerate(searchWord):
            if i == 0:
                continue
            lookingAtY = targetY + (vector[0] * i)
            lookingAtX = targetX + (vector[1] * i)

            if lookingAtY < 0 or lookingAtY >= len(grid):
                break
            if lookingAtX < 0 or lookingAtX >= len(grid[0]):
                break
            if grid[lookingAtY][lookingAtX] != letter:
                break
            if grid[lookingAtY][lookingAtX] == searchWord[-1]:
                foundWord = True
        if foundWord:
            total += 1

    return total

def SearchForX(grid, targetX, targetY):
    if targetX >= len(grid[0]) or targetY >= len(grid):
        return 0
    
    if targetX + 1 >= len(grid[0]) or targetX -1 < 0:
        return 0
    if targetY + 1 >= len(grid) or targetY -1 < 0:
        return 0

    hasX = False
    letter1 = grid[targetY + 1][targetX + 1]
    letter2 = grid[targetY - 1][targetX - 1]
    if (letter1 == "S" and letter2 == "M") or (letter1 == "M" and letter2 == "S"):
        letter1 = grid[targetY + 1][targetX - 1]
        letter2 = grid[targetY - 1][targetX + 1]
        if (letter1 == "S" and letter2 == "M") or (letter1 == "M" and letter2 == "S"):
            hasX = True
    
    if hasX == True:
        return 1
    else:
        return 0

input = open("Day4\input.txt").read().split()

totalXmas = 0
totalX_Mas = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == "X":
            totalXmas += SearchForWord(input, "XMAS", x, y)
        if input[y][x] == "A":
            totalX_Mas += SearchForX(input, x, y)

print("Part 1: " + str(totalXmas))
print("Part 2: " + str(totalX_Mas))