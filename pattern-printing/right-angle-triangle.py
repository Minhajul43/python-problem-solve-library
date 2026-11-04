n=int(input("Enter the base of the triangle:"))
m=int(input("Enter the height of the triangle:"))
for i in range(m):
    for j in range(i+1):
        print("*",end=" ")
    print()