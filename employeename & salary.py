def create_employee_dictionary(names, salaries):
    employee_dict = {}
    for i in range(len(names)):
        employee_dict[names[i]] = salaries[i]
    return employee_dict

names_input = input("Enter employee names separated by commas: ")
salaries_input = input("Enter corresponding salaries separated by commas: ")

names = names_input.split(',')
salaries = [int(s) for s in salaries_input.split(',')]

if len(names) != len(salaries):
    print("Error: Number of names and salaries must be the same.")
else:
    result_dict = create_employee_dictionary(names, salaries)

    print(result_dict)
