# fruits = {"apples", "bananas", "cherries"}
# numbers = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}

# Set operations:
# fruits.add("grapes")
# fruits.reverse()
# fruits.remove("bananas")
# fruits.discard("cherries")


# print(fruits)
# print("apples" in fruits) # to check if something is in a set

# Sets math operations:

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

# print(set2.union(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))

# Removes duplicates from a list:
# fruits = {"apples", "bananas", "cherries", "apples", "bananas"}
# print(fruits)

# Removing duplicates from a list using set:
# numbers = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 8]
# unique_numbers = set(numbers)
# print(unique_numbers)

# Exercise 1:
# 1. Create a system that stores students grades as tuples (name, subejct, grade) and uses sets to find uniques subjects and students.
# Student grades stored as tuples 

# Step1 - Store grades as tuples
# grades = [("Alice", "Math", 85),
#           ("Bob", "Math", 90),
#           ("Charlie", "Science", 95),
#           ("Bob", "Science", 80),
#           ("Charlie", "Math", 70),
#           ("Alice", "Science", 75)]

# Step 2 - use sets to find unique students and subjects

# students = set()
# for record in grades:
#     students.add(record[0])

# subjects = set()
# for record in grades:
#     subjects.add(record[1])

# score = set()
# for record in grades:
#     score.add(record[2])

# print("Unique students:", students)
# print("Unique Subjects:", subjects)
# print("Highest Score:", max(score))


# Find Alice's grades:
# alice_grades = []

# for grade in grades:
#     if grade [0] == "Alice":
#         alice_grades.append((grade[1], grade[2]))

# print("Alice's grades:", alice_grades)

# Exercise 2: 
# You are building a tiny system for a library. 

borrowed_books = []

# Find:
# 1. All unique people who borrowed books
# 2. All unique book titles
# 3. All unique genres
# BONUS: Count how many books each person borrowed

