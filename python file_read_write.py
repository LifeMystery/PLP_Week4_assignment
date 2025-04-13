def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (as an example, converting all text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Content has been successfully modified and saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask the user for the filename and output filename
    input_filename = input("Please enter the name of the file to read from: ")
    output_filename = input("Please enter the name of the file to write to: ")

    # Call the function to read and modify the file
    read_and_modify_file(input_filename, output_filename)


if __name__ == "__main__":
    main()
