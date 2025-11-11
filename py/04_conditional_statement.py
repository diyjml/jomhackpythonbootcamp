# if-else: 2 conditions
# if-elif-else: more than 2 conditions

# Example 1:

# age = 21

# if age >= 18:
#     print("You are an adult and of legal age.")
# else:
#     print("You are a minor!")

# Example 2:

# score = 95

# if score >+ 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >+ 70:
#     grade = "C"
# elif score >+ 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Your grade is: {grade}")    

# and: both conditions must be True
# or: at least one condition must be True 

# Example 3:

# user_age = 13
# has_license = True 

# if user_age>=18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")

# Example 4:

# day = "Sunday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the freakin' weekend!")
# else:
#     print("It's a boring weekday.")

# Nested Conditions: condition within condition

# Example 5:

# weather = "sunny" 
# temperature = 30 

# if weather == "sunny":
#     if temperature > 70:
#         print("It's a hot sunny day! I wanna stay indoors.")
#     else:
#         print("It's a pleasant sunny day! Let's go for a walk.")

# Exercise 1:

# Write a program that categorizes BMI (Body Mass Index) into underweight (<18.5), normal (<24.9), overweight (<29.9) and obese (>30.0). (Formula = kg/mˆ2)

# BMI Categorizer (Simple Version):
weight = 47
height = 1.52 

# Calculate BMI
bmi = weight / (height ** 2) 

# Categorize BMI:
if bmi <18.5:
    category = "Underweight"
elif bmi <24.9:
    category = "Normal weight"
elif bmi <29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is {bmi:.2f}")
print(f"Category: {category}")

# BMI Categorizer (Detailed Version):

# Step 1: Get user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Insert your height in meters: "))

# Step 2: Calculate BMI 
bmi = weight / (height ** 2)

# Step 3: Categorize BMI 
print(f"Your BMI is {bmi:.2f}")

if bmi <18.5:
    print("Category: Underweight")

elif bmi <24.9:
    print("Category: Normal weight")

elif bmi <29.9:
    print(f"Category: Overweight")
else: 
    print("Category: Obesity")
