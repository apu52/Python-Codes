x = int(input("ENTER A NUMBER: "))
y = int(input("ENTER ANOTHER NUMBER: "))

if x>y :
    smaller =y
else:
    smaller =x
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        GCD =i
print("GCD of ",x,"and",y,"=",GCD)