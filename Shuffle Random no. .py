#main code
import random
nums=[]
n = int(input("Enter total number of random numbers : "))
l1=int(input("Enter the lower range : "))
l2=int(input("Enter the upper range : "))
for i in range(n):
    nums.append(random.randint(l1,l2))
print("OriginalList : ",nums)
random.shuffle(nums)
print("Shuffled List : ",nums)
