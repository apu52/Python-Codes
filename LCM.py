def lcm(x, y):
    product = x * y

    while y:
        x, y = y, x % y

    lcm_result = product // x
    return lcm_result


num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))


result_lcm = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {result_lcm}")
