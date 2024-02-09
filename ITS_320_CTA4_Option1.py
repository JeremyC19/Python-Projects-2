maxSoFar = float(0)
minSoFar = float(0)
interest = float(0)
average = float(0)
total = float(0)
number = float(0)

count = int(0)

while count < 5:
    number = float(input("Enter a number "))
    total = total + number
    average = total/5
    if count == 0:
        maxSoFar = number
    elif number > maxSoFar:
        maxSoFar = number

    if count == 0:
        minSoFar = number
    elif number < minSoFar:
        minSoFar = number

    interest = float(total + total * 0.2)

    count = count + 1

print("The total of your 5 numbers is " + str(total))
print("The average of your 5 numbers is " + str(average))
print("The minimum of your numbers is " + str(minSoFar))
print("The maximum of your numbers is " + str(maxSoFar))
print("The total of your 5 numbers with 20 percent interest is " + str(interest))
