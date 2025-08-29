# File Read & Write Challenge with Error Handling

def process_file(filename):
    try:
        # Open the file and read its contents
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open("modified_output.txt", "w") as new_file:
            new_file.write(modified_content)

        print("File has been processed successfully! Check 'modified_output.txt'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for a filename
filename = input("Enter the filename to read: ")
process_file(filename)
