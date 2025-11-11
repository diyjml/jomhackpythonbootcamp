# single_quote = 'hello'
# double_quote = "world"
# triple_quote = """Multi-line
# string"""

# print(single_quote)
# print(double_quote)
# print(triple_quote) 

# text = "Python Programming"

# print(text[0])
# print(text[-1])
# print(text[0:6])
# print(text[:6])
# print(text[7:])

# name = "Johnn Doe"
# age = 30

# message_1 = f"My name is {name} and I am {age} years old."
# message_2 = "My name is {} and I am {} years old".format(name, age)
# message_3 = "Mu name is %s and I am %d years old." % (name, age)

# print(message_1)
# print(message_2)
# print(message_3)

# single_quote = 'Hello'
# double_quote = "World"
# triple_quote = """Multi-line
# string"""

# print(single_quote)
# print(double_quote)
# print(triple_quote) 

# single_quote = 'It is a nice day'
# double_quote = "He said, \"how you doin'?\""
# triple_quote = """She said, and I quote:
# "It's a beautiful world, we live in!" """

# print(single_quote)
# print(double_quote)
# print(triple_quote)

text = """Python is a powerful programming language. It's easy to learn and versatile!
You can use Python for web development, data science, and automation. The syntax is clean and readable. 
This makes Python perfect for beginners and experts alike."""

# Word Count
word_count = len(text.split())
print("Word Count:", word_count)

# Character Count
char_count = len(text)
print("Character Count:", char_count)

# Sentence Count
sentence_count = text.count(".") + text.count("!") + text.count("?")
print("Sentence Count:", sentence_count)