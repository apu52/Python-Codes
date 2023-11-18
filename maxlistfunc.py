find_max = lambda x: max(x)

def find_maximum_value(input_list):
    max_value = find_max(input_list)
    return max_value

user_input = input("Enter numbers separated by spaces: ")
numbers_list = [int(x) for x in user_input.split()]

maximum_value = find_maximum_value(numbers_list)

print("Maximum value:", maximum_value)
