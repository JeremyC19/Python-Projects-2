
color = input("Enter a Color: ")
pluralNoun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(pluralNoun + " are blue")
print("I love " + celebrity)

def reverse():
    string = input("Enter your first string: ")
    string2 = input("Enter your second string: ")
    string3 = input("Enter your third string: ")

    print("Your original three strings look like: " + string + " " + string2 + " " + string3)

    j = len(string)
    j2 = len(string2)
    j3 = len(string3)

    print("Your three strings reversed look like: ", end='')

    while j3 > 0:
        k3 = j3 - 1
        i3 = string3[k3]
        print(i3, end='')
        j3 = j3 - 1

    print(" ", end='')

    while j2 > 0:
        k2 = j2 - 1
        i2 = string2[k2]
        print(i2, end='')
        j2 = j2 - 1

    print(" ", end='')

    while j > 0:
        k = j - 1
        i = string[k]
        print(i, end='')
        j = j - 1

reverse()
print("")
reverse()
