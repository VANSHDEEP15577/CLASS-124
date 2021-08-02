array=[]
array2=[]
w=int(input("ENTER THE ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=int(input("ENTER THE ELEMENT:"))
    array.append(p)
    if p % 2 == 0:
        array2.append(p)
    else:
        pass
print(array)
print(array2)