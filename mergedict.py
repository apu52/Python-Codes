def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)  
    return merged_dict


num_pairs_dict1 = int(input("Enter the number of key-value pairs for the first dictionary: "))
dict1 = {}
for _ in range(num_pairs_dict1):
    key = input("Enter key: ")
    value = int(input("Enter corresponding value: "))
    dict1[key] = value
    
num_pairs_dict2 = int(input("Enter the number of key-value pairs for the second dictionary: "))
dict2 = {}
for _ in range(num_pairs_dict2):
    key = input("Enter key: ")
    value = int(input("Enter corresponding value: "))
    dict2[key] = value

result_dict = merge_dicts(dict1, dict2)

print("Merged Dictionary:", result_dict)
