def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calculate_lcm(x, y):
    lcm = (x * y) // calculate_gcd(x, y)
    return lcm

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        gcd_result = calculate_gcd(num1, num2)
        lcm_result = calculate_lcm(num1, num2)

        print(f"GCD of {num1} and {num2} is: {gcd_result}")
        print(f"LCM of {num1} and {num2} is: {lcm_result}")

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
