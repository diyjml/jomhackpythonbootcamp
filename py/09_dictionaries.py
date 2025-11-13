# students = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A",
#     "courses": ["Math", "Science", "English"]
# }

# Accessing values using keys:
# print(students["name"])
# print(students["age"])
# print(students["grade"])

# modifying and adding:
# print(students.get("age")) 
# students["age"] = 21 # modify value
# students["email"] = "alice@gmail.com" # add new key value 

# print(students)

# Dictionaries method:
# keys = students.keys()      # get all keys
# values = students.values()  # get all values
# items = students.items()    # get all items

# print(keys)
# print(values)
# print(items)

# # Iterating through dictionaries:
# for key in students:
#     print(f"{key}: {students[key]}")

# for key, value in students.items():
#     print(f"{key}: {value}")

# Nested dictionaries:
company = {
    "employees": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 30, "department": "HR"}
    },
    "departments": ["IT", "HR", "Finance"]
}

print(company["employees"].items())
print(company["departments"])
