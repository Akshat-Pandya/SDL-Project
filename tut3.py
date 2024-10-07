# Strings in python - 
# An of characters each character has an index number it starts from 0 and goes till length of the string minus 1 

# "Hello"
# 'Hello'
# '''Hello'''

s="Apple is red"
print(s)
print(s[3])

# String slicing 
print(s[6:8])

# Important functions - 
#len()
print(len("Hello")) # 5
#endswith()
s="Hello"
print(s.endswith("lo")) # True
#startswith()
print(s.startswith("He")) # Tre
#count()
s="CATASTROPE"
print(s.count('T'))
#capitalize a string
s="cat"
print(s.capitalize())

s="DOCTOR"
print(s.find("OCT"))


s="Hello World"

print(s.replace("World","Everyone"))
print(s)

# Strings are immutable in python.

# Escape sequences in pyton 
print("Hello\\World")
