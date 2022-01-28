# Menu keys
MENU_CHOICES = ['+', '-', '*', '/', 'm', 'q']
# The number of binary operations
NUMBER_OF_BINARY_OPERATIONS = 4
# Names of the first and the second arguments for binary operations
FIRST_NUMBER_NAMES = ['Summand 1: ', 'Minuend: ', 'Factor 1: ', 'Dividend: ']
SECOND_NUMBER_NAMES = ['Summand 2: ', 'Subtrahend: ', 'Factor 2: ', 'Divisor: ']
# Names of the results of binary operations
RESULT_NAMES = ['Sum:', 'Difference:', 'Product:', 'Quotient:']
# Binary functions to be called
CFUN2_FUNCTIONS = [cfun2_addition, cfun2_subtraction, cfun2_multiplication, cfun2_division]


# Main "worker" function
def main_dialog():
    # Return Boolean variable:
    #  True: continue
    #  False: quit
    ch = input("Your choice: ")
    try:
        ch_index = MENU_CHOICES.index(ch)
    except ValueError:
        print('That is not a valid choice.')
        print_main_menu()
        return True

    if ch_index < NUMBER_OF_BINARY_OPERATIONS:
        code, num1 = input_number(FIRST_NUMBER_NAMES[ch_index])
        if code < 2:
            return (code > 0)
        code, num2 = input_number(SECOND_NUMBER_NAMES[ch_index])
        if code < 2:
            return (code > 0)
        result = CFUN2_FUNCTIONS[ch_index](num1, num2)
        if isinstance(result, str):
            print(result)  # in case of error
        else:
            print(RESULT_NAMES[ch_index], result)  # in case of success
        return True



global_cont = True  # Whether to continue the dialog. If not, quit.

print_main_menu()
while global_cont:
    global_cont = main_dialog()


def main_dialog():
    # Return Boolean variable:
    #  True: continue
    #  False: quit
    ch = input("Your choice: ")
    try:
        ch_index = MENU_CHOICES.index(ch)
    except ValueError:
        print('That is not a valid choice.')
        print_main_menu()
        return True

    if ch_index < NUMBER_OF_BINARY_OPERATIONS:
        code, num1 = input_number(FIRST_NUMBER_NAMES[ch_index])
        if code < 2:
            return (code > 0)
        code, num2 = input_number(SECOND_NUMBER_NAMES[ch_index])
        if code < 2:
            return (code > 0)
        result = CFUN2_FUNCTIONS[ch_index](num1, num2)
        if isinstance(result, str):
            print(result)  # in case of error
        else:
            print(RESULT_NAMES[ch_index], result)  # in case of success
        return True
    else:
        ch_index:
            case 4:
                print_main_menu()
                return True
            case 5:
                print('Good bye!')
                return False


global_cont = True  # Whether to continue the dialog. If not, quit.

print_main_menu()
while global_cont:
    global_cont = main_dialog()





