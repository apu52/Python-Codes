is_even = lambda x: x % 2 == 0

def print_even_numbers(input_list):
    even_numbers = filter(is_even, input_list)
    print("Even numbers:", list(even_numbers))

user_input = input("Enter numbers separated by spaces: ")
numbers_list = [int(x) for x in user_input.split()]

print_even_numbers(numbers_list)
