def find_unique_elements(input_list):
    unique_elements = set()

    for element in input_list:
        unique_elements.add(element)
    return list(unique_elements)

user_input = input("Enter elements of the list separated by spaces: ")
input_list = [int(x) for x in user_input.split()]

unique_elements_list = find_unique_elements(input_list)

print("Original list:", input_list)
print("Unique elements:", unique_elements_list)
