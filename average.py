average = 0
total = 0
howManyEntered = 0

howMany = int(input ("How many numbers do you want to enter?"))
testscore = int(input ("enter test score: "))

total = total + testscore

howManyEntered = howManyEntered + 1

while howManyEntered < howMany:
    testscore = int(input ("enter test score: "))
    total = total + testscore
    howManyEntered = howManyEntered + 1

average = total / howMany

print("The average for the test score you entered is: ")
print(average)


    




