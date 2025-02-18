"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key. (almost all operations you do you'll use it's key)
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools  # is the key (Duke) in dictionary schools (if it is True if not false)
print(f"Duke is pressent {is_duke_present}.") 

# another way to test same as aboce
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal 
schools = {}  # Same as dict()
print(schools)

# Alternatively, initialze key-value pairs
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150
}

# Example looping over the keys of a dict
list = []
for key in schools.keys():
    list.append(key)     
print(list)

for school in schools:
    print(f"Key: {school} Key2: {list[1]}  -> Value: {schools[school]}")
print(schools)