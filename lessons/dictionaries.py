"""Demonstrating dictionary capabilities."""

#Declare dictionary with types
schools: dict[str, int]

#Initialize empty dictionary
schools = dict()

#Setting individual key-value pairings
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

#Prints dictionary literal
print(schools)

#Lookup value by key
print(schools["UNC"])

#Remove pair by key
schools.pop("Duke")

#See if key exists
is_duke_present: bool = "Duke" in schools

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")