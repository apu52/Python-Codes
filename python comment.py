def copy_python_script():
    src_file = input("Enter the path of the source Python script file: ")
    dest_file = input("Enter the path of the destination Python script file: ")

    try:
        # taking read mode from input file
        with open(src_file, 'r') as source:
        # write the code to another destination file
            with open(dest_file, 'w') as destination:
                for line in source:
                    # Skip comment lines start with #
                    if not line.lstrip().startswith('#'):
                        destination.write(line)
        
        print(f"Successfully copied content from {src_file} to {dest_file}, excluding comments.")
    except:
        print("An error occurred. Please check the file paths or other issues.")


copy_python_script()
