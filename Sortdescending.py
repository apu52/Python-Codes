def sort_dict_by_value(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict

num_pairs = int(input("Enter the number of key-value pairs: "))

input_dict = {}
for _ in range(num_pairs):
    key = input("Enter key: ")
    value = int(input("Enter corresponding value: "))
    input_dict[key] = value

sorted_dict = sort_dict_by_value(input_dict)

print("Original Dictionary:", input_dict)
print("Sorted Dictionary:", sorted_dict)
