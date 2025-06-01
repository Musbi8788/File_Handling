def show_cats_dogs_name(filename):
    """Show the cats and dogs name from the text file."""
    try:
        with open(filename, encoding='utf-8') as file_objects:
            content = file_objects.read()
    except FileNotFoundError:
        # Silent Fail
        pass
    else:
        print("The names in {}\n{}.".format(filename, content))
            

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    show_cats_dogs_name(filename)