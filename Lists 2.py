lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(-1, "Kelly")
friends.remove("Jim")
friends.pop()  # removes last element
print(friends.count("Jim"))
print(friends.index("Kevin"))  # returns index of element
print(friends)
lucky_numbers.append(1)
del lucky_numbers[3]
lucky_numbers[0] = 11
print(lucky_numbers)
lucky_numbers.sort()
lucky_numbers.reverse()
friends2 = friends.copy()
print(friends2)
friends.clear()
