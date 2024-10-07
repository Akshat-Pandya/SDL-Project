# types of loops : for loop , while loop


# # factorial using for loop
# num=int(input("Enter a number : "))
# result=1
# for i in range(1,num+1):
#     result*=i
# print(f"The factorial of {num}={result}")

# while loops



result=1
i=1
num=int(input("Enter a number : "))
while (i<=num):
    result*=i
    i+=1
print(f"The factorial of {num} is {result}")




# continue keyword ->skip the current iteration
for i in range(1,10):
    if i==5:
        continue
    else:
        print(i)


