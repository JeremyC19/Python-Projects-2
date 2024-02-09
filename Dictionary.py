
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(monthConversions["Jan"])
print(monthConversions.get("no", "not a valid key"))
monthConversions.update({"Feb":"April"})
monthConversions.pop("Jan")
monthConversions["May"] = "May"

print(monthConversions)

familyInformation = {
    "Aunt Mary": ["Mary", "Smith", "1001 Meadow Lane, New York, NY", "November 10, 1980"],
    "Grandpa John": ["John", "Park", "176 Grotto Drive, Seattle, WA", "June 8, 1951"],
    "Uncle Drew": ["Drew", "Park", "4820 Washington Street, Tacoma, WA", "March 23, 1982"]
}

print(familyInformation["Aunt Mary"][2])
print(familyInformation["Uncle Drew"][0])
print(familyInformation["Grandpa John"])
