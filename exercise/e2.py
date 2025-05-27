# file name
filename = 'guest.txt'

with open(filename, 'w') as file_objects:
    # get the username
    username = input("Enter your fullname: ")
    # store the username in a txt file.
    file_objects.write(username)