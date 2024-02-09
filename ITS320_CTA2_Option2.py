carBrand = input("What brand is your car? ")
model = input("What model is your car? ")
year = int(input("What year is your car? "))
startOdometer = int(input("What was your starting odometer reading? "))
endingOdometer = int(input("What was your ending odometer reading? "))
mpg = int(input("What is your estimated miles per gallon? "))

dictionary = {
    "Car Brand": carBrand,
    "Model": model,
    "Year": year,
    "Starting Odometer": startOdometer,
    "Ending Odometer": endingOdometer,
    "MPG": mpg,
}

print("Here are the details of your car: ")
print(dictionary)
