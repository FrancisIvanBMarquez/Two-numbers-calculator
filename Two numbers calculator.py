# Marquez, Francis Ivan B.,_BSCpE 1-5

# loop
try_again = 1
while try_again == 1:
    # choose operation / try catch
    operation_loop = 1
    while operation_loop == 1:
        try:
            operation = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))
        except ValueError:
            print("Please input an integer")
        except TypeError:
            print("Please enter 1,2,3 and 4 only")
            
        else:
            if operation < 1 or operation > 4:
                print("You have input a number less than 1 or more than 4, Please input 1, 2, 3 and 4 only")
            else:
                operation_loop = operation_loop - 1
    
    # ask two numbers / try catch
    first_number_loop = 1
    while first_number_loop == 1:
        try:
            first_number = float(input("Enter the first number: "))
        except ValueError:
            print("Please input an integer or a decimal only")
        else:
            first_number_loop = first_number_loop - 1

    second_number_loop = 1
    while second_number_loop == 1:
        try:
            second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Please input an integer or a decimal only")
        else:
            if operation == 4 and second_number == 0:
                print("Cannot divide by zero, Please input another number")
            else:
                second_number_loop = second_number_loop - 1


    # result
    result = ""
    if operation == 1:
        result = first_number + second_number
    elif operation == 2:
        result = first_number - second_number
    elif operation == 3:
        result = first_number * second_number
    else:
        result = first_number / second_number

    print("Your answer is: ", result)

        
    # update loop / try catch
    try_again_question = int(input("Do you want to try again? 1 for yes, 0 for no: "))
    if try_again_question == 1:
        pass
    else:
        try_again = try_again - 1
        # display thank you
        print("Thank you!")
