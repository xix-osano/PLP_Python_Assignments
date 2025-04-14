#  Ask the user for the filename
input_filename = input("Enter the filename to read: ")

try:
    # Open and read the file
    with open(input_filename, "r") as infile:
        data = infile.read()
        print("File content read successfully.")

    # Modify the data (for example, convert to uppercase)
    modified_data = data.upper()

    # Define the output file name
    output_filename = "modified_" + input_filename

    # Write the modified data to the new file
    with open(output_filename, "w") as outfile:
        outfile.write(modified_data)

    print(f"Modified data written to {output_filename}")

except FileNotFoundError:
    print("Error: The file does not exist.")