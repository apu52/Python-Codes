#module
def fat(n):
    pdt= 1
    for i in range(1,n+1):
        pdt*=i
    return pdt

#main code
import factorialModule as f
n = int(input("Enter a number : "))
facto = f.fat(n)
print(facto)
