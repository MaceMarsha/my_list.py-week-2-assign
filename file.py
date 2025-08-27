# File Read & Write Challenge with Error Handling

filename = input("Python learning: ")
try:
    with open(filename, 'r') as infile:
        content = infile.read()
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read the file.")
else:
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to {new_filename}")
    except IOError:
        print("Error: Could not write to the new file.")