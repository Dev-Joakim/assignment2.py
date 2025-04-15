def read_and_modify_file():
    # Ask user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Create a new filename for output
        new_filename = f"modified_{filename}"

        # Write the modified content to the new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read or write the file '{filename}'.")

# Run the function
read_and_modify_file()
