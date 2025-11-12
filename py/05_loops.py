# For Loops:
# for i in range(5):
#     print (i)

# for i in range(1, 6):
#     print(i)

# for i in range(0,10,2):
#     print(i)

# While Loop:
# count = 2
# while count < 5:
#     print(count)
#     count += 1

# Loop control statement:
# for i in range(10):
#     if 1 == 3:
#         continue 
#     if i == 7:
#         break 
#     print(i)

# # Nested loop:
# for i in range(3): 
#     for j in range(4):
#         print(f"({i}, {j})")

# Exercise 1:
# Create a multiplication table generator. 

# num = int(input("Enter a number: "))
# for i in range(1,10):
#     result = num * i
#     print(f"{num} x {i} = {result}")

# Exercise 2:
# Write a program that finds all the prime numbers up to a given number. (limit = 20)

limit = 20
for n in range(2, limit +1):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break 
    if is_prime:
        print(n)
