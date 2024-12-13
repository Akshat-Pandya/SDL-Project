#Basic Read operation
file=open("file_handling/sample.txt","r") # mentioning "r" is optional
content=file.read()
print(content)
file.close()

#Basic Write operation - When we open the file in "w" mode and write into it the old contents 
#of file are completely deleted. 
file=open("file_handling/sample.txt","w") # mentioning "w" is necessary
file.write("\nThis is line 5")
file.close()

#Basic Append operation - When we open the file in "a" mode and write into it the old content of the file remain
#unchanged and new ones are added
file=open("file_handling/sample.txt","a")
file.write("\nThis is a new line")
file.close()

#the with block is the professional way to deal with the files it removes the need to 
#explicitly close the file 

with open("file_handling/sample.txt","r") as f:
    print(f"The contents of the file : \n{f.read()}")


# Key Notes:
# Both "w" and "a" modes will create the file automatically if it is not present.
