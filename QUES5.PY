def sen(s):
    v={"UP":0,"LOW":0}
    for i in s:
        if s.isupper():
            v["UP"]+=1
        elif s.islower():
            v["LOW"]+=1
        else:
            pass
    print("ORIGINAL ARRAY: ",s)
    print("THE UPPER CASE CHARACTER'S ARE:",v["UP"])
    print("THE LOWER CASE CHARACTER'S ARE:",v["LOW"])
s=input("ENTER THE SENTENCE:")
sen(s)
