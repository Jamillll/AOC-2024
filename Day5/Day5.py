def main():
    input = open("Day5\input.txt").read().split()

    orderRules = list()
    updateNumbers = list()
    for line in input:
        if line.find("|") != -1:
            orderRules.append(line)
        else:
            updateNumbers.append(line)
    orderRules.sort()

    correctUpdateTotal = 0
    resolvedUpdateTotal = 0
    for update in updateNumbers:
        update = update.split(",")
        relevantRules = getRelevantRules(orderRules, update)

        evaluatedUpdate = [None] * len(update)
        for i, number in enumerate(update):
            ruleCount = 0
            for rule in relevantRules:
                if rule[0] == number:
                    ruleCount += 1 
            evaluatedUpdate[ruleCount] = number
        evaluatedUpdate.reverse()

        print(update)
        print(evaluatedUpdate)
        if update == evaluatedUpdate:
            correctUpdateTotal += int(update[(len(update) // 2)])
            print("Match!")
        else:
            resolvedUpdateTotal += int(evaluatedUpdate[(len(evaluatedUpdate) // 2)])

    print("Part 1, correct update total: " + str(correctUpdateTotal))
    print("Part 2, resolved update total: " + str(resolvedUpdateTotal))

def getRelevantRules(orderRules, updateNumbers):
    relevantRules = list()

    for rule in orderRules:
        rule = rule.split("|")
        hasFoundFirstNumber = False
        hasFoundSecondNumber = False

        for number in updateNumbers:
            if number == rule[0]:
                hasFoundFirstNumber = True
            if number == rule[1]:
                hasFoundSecondNumber = True

        if hasFoundFirstNumber and hasFoundSecondNumber:
            relevantRules.append(rule)
            continue
    return relevantRules      


if __name__ == "__main__":
    main()