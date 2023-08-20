n=(int)(input("Enter the number of lines: "))

for i in range(1,n+1):
    sapces=n-i
    stars=(2*i)-1

    print(" " * sapces, end="")

    if i==1:
        print("1")
    else:
        print(str(i)+"*"*(stars-2)+str(i))