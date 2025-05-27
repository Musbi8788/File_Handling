filename = 'guest_book.txt'

with open(filename, 'a') as file_objects:
    guest_still_coming = True
    while guest_still_coming:
        username = input('What\'s your name? ')
        print(f"Hello {username}.")
        guest_book = input('Enter the book you finished reading: ')
        file_objects.write(f'Guest Book: {guest_book}\n')
        exist = input('Type [x] to exist or [c] to continue: ').lower()

        if exist == 'x':
            guest_still_coming = False

        else:
            valify = input('Are you sure you want to continue [yes/ or no]').lower()
            if valify == 'yes':
                guest_still_coming = True
            else:
                guest_still_coming = False