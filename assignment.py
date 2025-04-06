try:
    # Ask the user for the file name
    file_name = input("Enter the file name to read: ")

    # Open and read the file
    with open(file_name, "r") as file:
        content = file.read()

    # Modify the content by appending a message
    new_content = content + "\n-- file handling and exception handling --"

    # Write the modified content to a new file
    new_file_name = "new_" + file_name
    with open(new_file_name, "w") as new_file:
        new_file.write(new_content)

    print("Modified content saved to:", new_file_name)

except FileNotFoundError:
    print("Oops! File not found.")
except:
    print("Something went wrong. Please try again.")