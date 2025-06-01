# Define the text file to analyze
filename = 'count.txt'

# Open the file and read its contents
with open(filename, encoding='utf-8') as objects_file:
    # Read the entire contents of the file
    content = objects_file.read()
    # Count how many times "the " (with space) appears in the file
    count_the = content.lower().count('the ')
    # Display the result
    print(f"[[ The ]]  appears in the file {count_the} times.")
