def create_square_dictionary(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict

n = int(input("Enter a positive integer (n): "))

if n < 1:
    print("Please enter a positive integer.")
else:
    result_dict = create_square_dictionary(n)

    print(result_dict)
