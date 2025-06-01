
def count_words(filename):
    """Count the approximate number in a file"""
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else: 
        word = content.split()
        num_of_word = len(word)
        print(f"The file {filename} has about {num_of_word} number of words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)