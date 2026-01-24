# Define the file name
filename = "sample.txt"

try:
    # Open the file in read mode ('r')
    # Using 'with' is better because it automatically closes the file for you
    with open(filename, "r") as file:
        
        print(f"Reading content from {filename}:")
        print("-" * 30)
        
        # Loop through each line in the file
        for line in file:
            # .strip() removes the extra newline character from the file
            print(line.strip())
            
except FileNotFoundError:
    # This block runs if the file doesn't exist
    print(f"Error: The file '{filename}' was not found. Please create it first.")