#module
def prime(a):
    flag = 0
    for i in range (2,a):
        if a % i == 0:
            flag = 1
            break
    return flag
  
  #main code
  import primeModule as p
l1 = int(input("Enter lower limit: "))
l2 = int(input("Enter upper limit: "))
c=0
for i in range(l1+1,l2):
    if p.prime(i) == 0:
        print(i, end = " ")
        c+=1
if c==0 :
    print("There are no prime numbers between", l1,"&",l2)
