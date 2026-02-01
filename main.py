# day 3
# import pandas  # This is an example of external module
# import hashlib  # This is an example of built in module

# print("hi")

# Dont worry about how to use these modules just yet!
# pandas.read_csv("one.csv")
# m = hashlib.sha256()

#  day 4
# print("hi")

# day 5
# Single-Line Comments:
# Multi-Line Comments:
# Escape Sequence Characters
# More on Print statement
 
# day 6
# Variables and Data Types

#  day 10
# Taking User Input in Python

# a = int(input("square of your no. is "))
# print(a**2)

# day 11
# Strings In Python
# Quotation 
# Multiline string
# 
# a = "Strings"
# for char in a:
#     print(char)

# day12
# Strings Slicing and Operations on Strings in Python
# 1.Slicing from Start/End
# 2.Negative Indexing
# 3.Common String Operations
# name = "Siddhi"
# Length	len(name)	6
# Uppercase	name.upper()	SIDDHI
# Lowercase	name.lower()	siddhi
# Replace	name.replace("S", "K")	Kiddhi
# Check Prefix	name.startswith("S")	True

# day 13 
# String Methods in Python
# .upper() & .lower(): Converts the entire string to uppercase or lowercase.
# .title(): Capitalizes the first letter of every word.
# .capitalize(): Capitalizes only the very first letter of the string.
# .swapcase(): Flips lowercase to uppercase and vice-versa.
# .strip(): Removes all leading and trailing whitespace. (Very useful for CSV data!)
# .replace("old", "new"): Replaces all occurrences of a substring with another.
# .find("text"): Returns the index of the first occurrence of a word. Returns -1 if not found.
# .count("char"): Counts how many times a specific character or word appears.
# .isalpha(): Returns True if the string contains only letters (no numbers/spaces).
# .isdigit(): Returns True if the string contains only numbers.
# .islower() / .isupper(): Checks the casing of the string.
# .startswith("prefix") / .endswith("suffix"): Checks the beginning or end of a string.
# .split(","): Breaks a string into a list based on a separator.
# " ".join(list): Takes a list and combines it into one string with a space (or any character) between items.

# day14
# If Else Conditional Statements in Python
# if-else statements allow your program to make decisions. 
# They execute different blocks of code based on whether a condition is True or False.
# The elif Statement (Multiple Conditions)
# If you have more than two possibilities, use elif (short for "else if"). 
# Python checks these in order from top to bottom.
# Comparison Operators
# To create conditions, you'll use the common operators
# name = "Viddhi"

# if name.startswith("S"):
#     print("This name starts with S!")
# elif name.startswith("A"):
#     print("This name starts with A!")
# else:
#     print("This name starts with something else.")

# day16
# Match Case Statements in Python
# command = "save"

# match command:
#     case "open":
#         print("Opening file...")
#     case "save":
#         print("Saving file...")
#     case "exit":
#         print("Closing program...")
#     case _:
#         print("Unknown command")

# Matching Multiple Patterns

# day = "Saturday"
# match day:
#     case "Saturday" | "Sunday":
#         print("It's the weekend! 🎉")
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print("It's a workday. 💻")
# You can use the pipe symbol (|) to match multiple values in a single case,
# which is much cleaner than using or in an if statement.

# Match Case with Conditions (Guards)

# age = 21

# match age:
#     case n if n < 13:
#         print("Child")
#     case n if n < 20:
#         print("Teenager")
#     case _:
#         print("Adult")
# You can add an if statement to a case for even more control. 
# This is called a Guard.

