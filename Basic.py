
studentID = {
    "101": "Jayanta Biswas",
    "102": "Rony Debnath",
    "103": "Araf Karim",
    "104": "Baki Billaha",
    "105": "Joy Ali",
}

# show
print(studentID)
print(studentID["103"])
# error
# print(studentID["106"])
print(studentID.get("104"))
print(studentID.get("106")) # none
print(studentID.get("106", "Key doesn't exists."))

# Updating Dictionary
studentID["103"] = "Araf Ali"
print(studentID)

# Delete Dictionary Elements
del studentID["101"] # remove an element
print(studentID)

studentID.clear() # remove all elements
print(studentID)

del studentID # delete dictionary
print(studentID)

