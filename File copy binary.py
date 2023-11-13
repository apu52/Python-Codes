def copy_binary_file():
    try:
        input_file_path = input("Enter the path of the input binary file: ")
        output_file_path = input("Enter the path of the output binary file: ")
        num_bytes = 100

        with open(input_file_path, 'rb') as in_file:
            with open(output_file_path, 'wb') as out_file:
                data = in_file.read(num_bytes)
                out_file.write(data)
                print(f"Successfully copied {num_bytes} bytes from {input_file_path} to {output_file_path}")
    except FileNotFoundError:
        print("File not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_binary_file()








