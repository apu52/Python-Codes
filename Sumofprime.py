print("Example range of numbers: a to b")
a=(int)(input("Enter value of a: "))
b=(int)(input("Enter value of b: "))
sum=0   
prime=True

for i in range(a,b):
    if(i>1):
        prime= True
    if(i==1):
        prime= False
        
    for j in range(2,int(i ** 0.5)+1):
        if(i%j==0):
            prime= False
            break
    if(prime):
        sum+=i
    
print("The sum of all the prime numbers in that given range is",sum)