# File Read & Write Challenge + Error Handling Lab

def modify_content(content):
    """
    Function to modify file content.
    (Example: make text uppercase)
    """
    return content.upper()


def main():
    # Ask the user for a filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening the file for reading
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"✅ Modified content written to {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
