import re

input = open("Day3\input.txt").read()
regexInput = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", input)
total = 0
commandsEnabled = True
for line in regexInput:
    if line == "do()":
        commandsEnabled = True
        continue
    elif line == "don't()":
        commandsEnabled = False
        continue

    if commandsEnabled:
        line = re.split(",", line)
        firstNumber = int(re.sub("\D", "", line[0]))
        secondNumber = int(re.sub("\D", "", line[1]))
        total += firstNumber * secondNumber

print(total)