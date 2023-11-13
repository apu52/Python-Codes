def all_substrings(input_string):
    substrings = []
    n = len(input_string)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(input_string[i:j])
    
    return substrings

input_str = input("Enter a string: ")

result = all_substrings(input_str)

print(f"All substrings of '{input_str}':")
print(result)
