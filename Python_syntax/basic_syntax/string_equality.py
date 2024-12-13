# In Python, you can check the equality of two strings using the equality operator (==) or the != operator for inequality. Here's how it works:

# Syntax:
# Equality Check: string1 == string2
# Inequality Check: string1 != string2

# Define two strings
string1 = "Hello"
string2 = "hello"
string3 = "Hello"

# Check for equality
print(string1 == string2)  # False (case-sensitive)
print(string1 == string3)  # True (exact match)

# Check for inequality
print(string1 != string2)  # True (they are not the same)
print(string1 != string3)  # False (they are the same)

# Case-Insensitive Comparison
# If you want to compare strings without considering their case, you can convert both 
# strings to the same case (either lowercase or uppercase) using .lower() or .upper()

# Case-insensitive comparison
print(string1.lower() == string2.lower())  # True
