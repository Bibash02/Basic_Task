
try:
    file_name = input("Enter the file name: ")

    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    print(f"The file '{file_name}' contains {word_count} words.")
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")