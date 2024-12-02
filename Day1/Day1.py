input = open("Day1\input.txt")
list1 = list()
list2 = list()

for line in input:
    number1 = str()
    number2 = str()
    firstDone = False

    for i in line:
        if i == " " or i == "\n":
            firstDone = True
            continue
        
        if firstDone:
            number2 += i
        else:
            number1 += i

    list1.append(int(number1))
    list2.append(int(number2))

list1.sort()
list2.sort()

totalDistance = 0
for i, number in enumerate(list1):
    if number >= list2[i]:
        totalDistance += number - list2[i]
    else: 
        totalDistance += list2[i] - number

print("Total Distance = " + str(totalDistance))

# Part 2

similarityScore = 0
for number1 in list1:
    matchCount = 0
    for number2 in list2:
        if number2 == number1:
            matchCount += 1
    
    similarityScore += number1 * matchCount

print("Similarity Score = " + str(similarityScore))
