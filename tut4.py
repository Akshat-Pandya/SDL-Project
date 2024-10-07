#Lists are a containers to store a set of values of any datatype

list=["Hello",213,"World",124.24,True,None]
print(list)
print(list[2])

#slicing in the list
print(list[1:4])

#important methods in list
list=[1,32,4,331,41,4,62,356,5]
list.sort()
print(list)
list.reverse()
print(list)
list.append(100)
print(list)

list.insert(2,500)
print(list)

list.pop(2)
print(list)

list.remove(331)
print(list)

#tuples in python
t=(1,232,1,12)
print(t)

#important methods used in tuples
print(t.index(232))
print(t.count(1))
print(sum(t))