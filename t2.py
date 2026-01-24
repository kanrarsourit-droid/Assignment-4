# 1. Take user input and write it to the file
# Using 'w' mode (this will create the file or overwrite it if it exists)
filename = "output.txt"

initial_text = input("Enter the first line of text to save: ")
with open(filename, "w") as file:
    file.write(initial_text + "\n")

# 2. Append additional data to the same file
# Using 'a' mode (this adds to the end without deleting what's already there)
additional_text = input("Enter some more text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")

# 3. Read and display the final content
# Using 'r' mode
print("\n--- Current File Content ---")
with open(filename, "r") as file:
    content = file.read()
    print(content)