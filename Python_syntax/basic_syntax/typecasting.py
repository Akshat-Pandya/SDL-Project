
num=30
datatype=type(num)
print(datatype) # class <int>


num="30"
datatype=type(num)
print(datatype) # class <str>

num=30.2
datatype=type(num)
print(datatype) # class <float>

# Given that the conversion is valid you can convert any datatype variable to any other data
# type
num="100"
x=int(num) # takes any variable as input and convert s it to integer
print(x,':',type(x))
# Similarly there are float() , str() functions 
