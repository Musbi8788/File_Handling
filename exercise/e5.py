game_is_on = True

while game_is_on:

    # Get the user's two numbers
    print('Type "q" to exit.')

    num1 = input('Enter a First Number: ').lower()
    if num1 == 'q':
        break
        
    num2 = input('Enter a Second Number: ').lower()
    if num2 == 'q':
        break

    try: 
        # Try to add the number
        result = int(num1) + int(num2)
    except ValueError:
        # # Tell the user invalid input
        print("Invalid input you are adding [ {} to {} ].\n".format(num1, num2))
     
    else:
        # Show the result if successfull.
        print("The Result for {} + {} = {}.\n".format(num1, num2, result))
        
    

