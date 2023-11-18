is_divisible_by_5_and_7 = lambda x: x % 5 == 0 and x % 7 == 0

def find_numbers(start, end):
    divisible_numbers = [num for num in range(start, end + 1) if is_divisible_by_5_and_7(num)]
    return divisible_numbers

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = find_numbers(start_range, end_range)

print(f"Numbers divisible by 5 and 7 between {start_range} and {end_range}: {result}")
