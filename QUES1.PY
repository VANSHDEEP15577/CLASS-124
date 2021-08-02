a=int(input("ENTER THE 1ST NO:"))
d=int(input("ENTER THE 2ST NO:"))
c=int(input("ENTER THE 3ST NO:"))
if a>d and a>c:
    print(a,"IS GREATER THAN ",d , c)
elif d>a and d>c:
    print(d,"IS GREATER THAN ",c , a)
else:
    print(c,"IS GREATER THAN ",d , a)
