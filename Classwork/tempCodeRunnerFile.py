x=int(input("Enter a number"))
if x>0:
  print("YES")

else:
  print("No")


name =input("Enter your name: ")
nep =int(input("Enter nep mark: "))
eng =int(input("Enter eng mark: "))
mat =int(input("Enter mat mark: "))

total = nep+eng+mat
grade=""
if total>250:
    print(f"Name:{name} , Excellent")
elif total>=150 and total<250:
    print(f"Name:{name} Good")
else: 
    print(f"Name:{name} Work Hard")