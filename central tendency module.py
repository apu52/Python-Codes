#main code
import random
import math
n = int(input("Enter total number of random numbers (n<=10) : "))
randomlist = random.sample(range(1, 11), n)
randomlist.sort()
mean = 0
median = 0 
if n%2==1:
    median= randomlist[((n+1)//2)-1]
else :
    a=n//2
    b=a+1
    median = (randomlist[a-1]+randomlist[b-1])/2
for i in randomlist:
    print(i,end=" ")
    mean += i
var =0 
print()
mean = mean/n
for i in randomlist:
    var = var + (i-mean)**2
var = var/n
print("Mean =",mean)
print("Median =",median)
print("Standard Deviation :",math.sqrt(var))

