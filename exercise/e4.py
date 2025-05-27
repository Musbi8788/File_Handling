filename = 'programming_poll.txt'

with open(filename, 'a') as file_objects:
    still_polling = True
    ten_pro = 10 
    while still_polling:
        print(ten_pro)
        if ten_pro  > 0: 
            programmer_reason = input('Why did you like programming? ')
            file_objects.write(f'Reason: {programmer_reason}\n')
            ten_pro -= 1

        else:
            still_polling = False
        
        