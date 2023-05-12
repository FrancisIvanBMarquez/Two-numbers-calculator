# Marquez, Francis Ivan B.,_BSCpE 1-5

# loop
try_again = 1
while try_again == 1:
    # choose operation / try catch
    operation = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: "))

    # ask two numbers / try catch
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

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
