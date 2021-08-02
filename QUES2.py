array=[]
sum=0
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=int(input("ENTER THE ELEMENT:"))
    array.append(p)
    sum=sum+p
print(sum)