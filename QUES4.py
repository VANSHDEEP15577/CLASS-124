w=int(input("ENTER THE STARTING NO. OF THE RANGE:"))
p=int(input("ENTER THE ENDING NO. OF THE RANGE:"))
n=int(input("ENTER THE NO. YOU WANT TO CHECK:"))
if n < p and n > w:
    print(n,"FALLS IN ",w , p)
else:
    print(n,"DO NOT FALLS IN ",w , p)
