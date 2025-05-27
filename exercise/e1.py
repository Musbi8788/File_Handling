with open('learning_python.txt') as file_objects:
    lines = file_objects.readlines()
    
for line in lines:
        # Replacing a world in python by using the replace method()
        replace = line.replace('python', 'c')
        print(replace.strip())
        