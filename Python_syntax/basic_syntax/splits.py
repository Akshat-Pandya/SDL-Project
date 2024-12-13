# In Python, you can split a string based on a delimiter using the .split() method,
# similar to Java's split("").
# Syntax:
# string.split(delimiter) For example : 

text = "apple,banana,cherry"
delimiter = ","
result = text.split(delimiter)
print(result)

# Output : ['apple', 'banana', 'cherry']

# You can limit the number of splits using the maxsplit parameter:
# Syntax:
# string.split(delimiter,maxsplit) For example : 
text = "apple-banana-cherry-dog"
result = text.split("-", 2)  # Split at most 2 times
print(result)
# ['apple', 'banana', 'cherry-dog']

# Converting a string into an array/list of characters 
s="Hello"
char_array=list(s)
print(char_array)

# Note : list is a general function and not a part of string class. 




