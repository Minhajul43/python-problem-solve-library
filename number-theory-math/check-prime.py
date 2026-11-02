n=int(input("Enter a number: "))
for i in range(2,int(n**0.5)+1):
  if n%i==0:
    print(f" The {n} number is Not prime")
    break
else:
  print(f" The {n} number is Prime")