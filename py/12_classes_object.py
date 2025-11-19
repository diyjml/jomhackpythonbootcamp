# # Basic Class Definition 
# class Person:
#     # Class attribute (shared by all instances)
#     species = "Homo sapiens"

#     # Constructor Method 
#     def __init__(self, name, age):
#         # Instance Attributes 
#         self.name = name
#         self.age = age 

#     # Instance Method
#     def introduce(self):
#         return f"Hi, I'm {self.name} and I'm {self.age} years old."
        
#      #Method with parameters 
#     def have_birthday(self):
#         self.age += 1
#         return f"Happy birthday! {self.name} is now {self.age} years old."

# # Creating Objects (instances) 
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)

# #Accessing Attributes 
# print(person1.name)
# print(person1.age)

# # calling methods
# print(person1.introduce())
# print(person1.have_birthday())
# print(person2.introduce())
# print(person2.have_birthday())

# # class attributes
# print(Person.species)   # "Homo sapiens"
# print(person1.species)  # "Home sapiens"

# -----

# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_history.append(f"Deposited ${amount})")
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid deposit amount."
        
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance: 
#             self.balance -= amount 
#             self.transaction_history.append(f"Withdrew ${amount}")
#             return f"Withdrew ${amount}. New balance is ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds."
        
#     def get_balance(self):
#         return f"Current balance: ${self.balance}"
    
#     def get_transaction_history(self):
#         return self.transaction_history 
    
# # Using the BankAccount class 
# account = BankAccount("12345", "Alice", 1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())

#_____________________
# Exercise: Create a simple game character class with health, attack and heal methods. 

class Character:
    def __init__(self, name, health):
        # Attributes
        self.name = name
        self.health = health 

#Methods (self attack & heal)
    def attack(self, target, damage):
        target.health -= damage 
        print(f"{self.name} attacked {target.name} for {damage} damage.")
    
    # def heal(self, amount):
    #     self.health += amount
    #     print(f"{self.name} healed for {amount}. HP increased to {self.health}.")

#Creating Objects
player = Character("Knightingale", 100)
enemy = Character("Goblin", 100)


# Using the methods
player.attack(enemy,20)
# enemy.heal(10)

print(player.health)
print(enemy.health)
