# name = input("Enter your name:")
# height = float(input("Enter your height:"))

# # Input Validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Age must be positive!")
#     except ValueError:
#             print("Please enter a valid number!")

# # Output Validation:

# print(f"Hello, {name}!")
# print(f"You are {age} years old and {height} cm tall.")

# Exercises:
# 1. Create a simple calculator that takes two number and an operation from user.

# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         operation = input(("Enter operation (+, -, *, /): "))

#         if operation == '+' :
#             result = num1 + num2
#         elif operation == '-' :
#             result = num1 - num2
#         elif operation == '*' :
#             result = num1 * num2
#         elif operation == '/':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 print("Error: Cannot divide by zero!")
#                 continue
#         else:
#             print("Invalid operation!")
#             continue

#         print(f"The result is: {result}")
#         break

    # except ValueError:
    #     print("Please enter valid numbers!")

# 2. Create a simple quiz program with 3 questions.At the end of the quiz, display score. 

score = 0

# Question 1: 

answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct! ")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris. ")

# Question 2:
answer2 = input("What is 100 + 57? ")
if answer2 == "157":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The answer is 157. ")
    

# Question 3:
answer3 = input("What colour do you get when you mix blue and yellow? ").lower()
if answer3 == "green":
    print("Correct! ")
    score += 1
else:
    print("Wrong! The answer is green. ")
    

# Final Score:
print(f"Your final score is: {score}/3")
if score == 3:
    print("Perfect score! Well done!")
elif score >= 2:
    print("Good job!")
else:
    print("Better luck next time!")