n=int(input("Enter the number of rows:"))
spaces=n-1
for i in range(1,n+1):
  print(" " * spaces, end="")
  spaces -= 1
  for j in range(1,i+1):
    print(j,end=" ")
    print(spaces * " ", end="")
    spaces += 1
    print()
  