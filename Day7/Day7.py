import sys

def main(argv):
    input = open(argv[1]).read().split("\n")

    total = 0
    count = 1
    for line in input:
        line = line.split(":")
        result = int(line[0])
        numbers = [int(number) for number in line[1].split()]

        trinaryList = (len(numbers) - 1) * [0]

        checkCount = [0]
        if CombinationMarch(result, trinaryList, numbers, checkCount):
            total += result
            print("Pass")
        else:
            print("Failed")
        print(count)
        count += 1
    print(total)
    
            
def CheckEquation(desiredResult, trinaryList, numbers, checkCount) -> bool:
    total = 0
    checkCount[0] += 1
    for i, number in enumerate(numbers):
        if i == 0:
            total += number
            continue
        
        if trinaryList[i-1] == 0:
            total = total * number
        elif trinaryList[i-1] == 1:
            total += number
        elif trinaryList[i-1] == 2:
            total = int(str(total) + str(number))
    return total == desiredResult

def CombinationMarch(result, trinaryList, numbers, checkCount, depthValue = 0, increasing = True):
    if depthValue >= len(trinaryList):
        return False
    
    if not CheckEquation(result, trinaryList, numbers, checkCount):
        trinaryList[depthValue] = IncreaseTrinaryValue(trinaryList[depthValue])
        if depthValue != 0:
            if CombinationMarch(result, trinaryList, numbers, checkCount, depthValue - 1, False):
                return True
            if not increasing and depthValue == 0:
                return False   
        if not CheckEquation(result, trinaryList, numbers, checkCount):
            trinaryList[depthValue] = IncreaseTrinaryValue(trinaryList[depthValue])
            if depthValue != 0:
                if CombinationMarch(result, trinaryList, numbers, checkCount, depthValue - 1, False):
                    return True
                if not increasing and depthValue == 0:
                    return False    
            if not CheckEquation(result, trinaryList, numbers, checkCount):
                trinaryList[depthValue] = IncreaseTrinaryValue(trinaryList[depthValue])
                if depthValue != 0:
                    if CombinationMarch(result, trinaryList, numbers, checkCount, depthValue - 1, False):
                        return True
                    if not increasing and depthValue == 0:
                        return False
                if not CheckEquation(result, trinaryList, numbers, checkCount):
                    if depthValue != 0:
                        if CombinationMarch(result, trinaryList, numbers, checkCount, depthValue - 1, False):
                            return True
                    if increasing:
                        if CombinationMarch(result, trinaryList, numbers, checkCount, depthValue + 1):
                            return True
                    if not increasing and depthValue == 0:
                        return False
                else: return True
            else: return True
        else: return True
    else: return True
    return False

def IncreaseTrinaryValue(value):
    if value == 2:
        return 0
    else:
        return value + 1

if __name__ == "__main__":
    main(sys.argv)

# if equation doesn't work
# try new equation
# if new equation doesn't work
# is there previous equations
# if there is try them
# if there is not try next equations
# if no more equations to try, false

#111