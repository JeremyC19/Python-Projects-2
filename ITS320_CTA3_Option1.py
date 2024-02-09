year = int(input('What year do you want to know the value of the Ferrari 250 GTO? '))

if year < 1962:
    print("Invalid Year")
elif year <= 1964:
    print("The estimated value was $18,500.")
elif year <= 1968:
    print("The estimated value was $6,000")
elif year <= 1971:
    print("The estimated value was $12,000")
elif year <= 1975:
    print("The estimated value was $48,000")
elif year <= 1980:
    print("The estimated value was $200,000")
elif year <= 1985:
    print("The estimated value was $650,000")
elif year <= 2012:
    print("The estimated value was $35,000,000")
elif year <= 2014:
    print("The estimated value was $52,000,000")
elif year > 2014:
    print("The estimated value is unknown.")

print(3 and 0)
