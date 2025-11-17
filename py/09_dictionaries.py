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

# Loop through key and value:
# for key in students:
#     print(key)

# for value in students.values():
#     print(value)

# Key value pairs: (value returns only 1, while items return pairs which is key and value)
# for key, value in students.items():
#     print(key, value)


# # Iterating through dictionaries:
# for key in students:
#     print(f"{key}: {students[key]}")

# for key, value in students.items():
#     print(f"{key}: {value}")

# Nested dictionaries:
# company = {
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "jane": {"age": 30, "department": "HR"}
#     },
#     "department": ["IT", "HR", "Finance"]
# }

# print(company["employees"].items())
# print(company["departments"])

# Nested, clean f-string version: (it tells Python that if you see something, treat it as a variable instead of a text)
# for name, details in company["employees"].items():
#     print(f"employees: {name}, Age: {details['age']}, department: {details ['department']}")
     

# Exercise 1:
# Create a dictionary called student_records with the following information:
# "student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78]
# "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95]

student_records = {
    "student_001": {
        "Name": "John", 
        "Age": 19,
        "Major": "Computer Science",
        "Grades": [85, 92, 78]
    },
    "student_002": {
        "Name": "Sarah",
        "Age": 20,
        "Major": "Biology",
        "Grades": [90, 88, 95]
    }
}
# Exercise 2: 
# Add a new student "student_003" with name "Mike", age 18, major "Math", grades [82, 79, 91] 

# student_records["student_003"] = {
#     "Name": "Mike",
#     "Age": 18,
#     "Major": "Math",
#     "Grades": [82, 79, 91]
# }

# Exercise 3:
# Update John's age to 20 
# student_records["student_001"]["age"]= 20 

# Exercise 4: 
# Loop through the dictionary and print each student's information in this format:
# "student ID: [id], Name: [name], Major: [major]"

# print("Student IDs:", list(student_records.keys()))

# for student_id, details in student_records.items():
#     print(f"Student ID: {student_id}, Name: {details['Name']}, Major: {details['Major']}")

# Exercise 5:
# Calculate Sarah's average grade
sarah_grades = student_records["student_002"]["Grades"]
sarah_average = sum(sarah_grades) / len(sarah_grades)

print(f"Sarah's average grades: {sarah_average:.1f}")


# Exercise: Product Inventory System

# You will create:

# A list of product entries. Each product entry is a tuple containing: (product_name, category, stock_quantity)
# inventory = [
#     ("Shampoo", "Personal Care", 50)
#     ("Toothpaste", "Personal Care", 25)
#     ("Apples", "Food", 3)
#     ("Bananas", "Food", 7)
#     ("Detergen", "Cleaning Supplies", 15)
# ]

# Convert the list into a dictionary where
# key = product name
# value = stock quantity

# inventory_dict = {}
# for product, category, stock in inventory:
#     inventory_dict[product] = stock 

# Use a set to find all unique categories.

# Use a loop to print a report.