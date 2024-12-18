import os

def pcls():
    os.system("cls" if os.name == "not" else "clear")


def fstatement(name):
    while True:
        pcls()
        print(f"\nHello, {name}! Welcome in printing in Python")
        print("\n\nPython print() function prints the message to the screen or any other standard output device.")
        print("You can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function.")
        print("These parameters are represented as strings by their respective str() functions. To create a single output string, the transformed strings are concatenated with spaces between them.")
        print("String literals in Pythons print statement are primarily used to format or design how a specific string appears when printed using the print() function.")
        print("This string literal is used to add a new blank line while printing a statement.")
        print("An empty quote ('') is used to print an empty line.")
        print("The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function. ")

        print("Menu in printing in Python: ")
        print("1). Simple Printing")
        print("2). Back to Menu ")
        print("\n===========================================================")

        cstatement = input("\nPick a number from 1-2: ")

        if cstatement == "1":

            print("Input:")
            print("""print("Hello, World!")""")
            print("Output:")
            print("Hello, World!")

        elif cstatement == "2":
            print("\nReturning to the Main Menu...")
            return
        else:
            print("Invalid input. Please select from options 1-2.")


def Pvariables(name):
    while True:
        pcls()
        print(f"Hello, {name}! Welcome to Variables in Python")
        print("\n\tVariables are containers for storing data values.")

        print("\nMenu in variables in Python: ")
        print("\n1). Example variable")
        print("\n2). Back to main menu")
        print("\n================================================")

        variables = input("\nPick a number from 1-2: ")

        if variables == "1":

            print("\nInput:")
            print(""":""\tname: Althea
\tage: 19
\tprint(x)
\tprint(y)""")
            print("\nOutput: ")
            print("\tAlthea \n\t19")
            input("\nClick Enter to return to the menu...")
        elif variables == "2":
            print("\nReturning to the Main Menu...")
            return
        else:
            print("Invalid input. Please select from options 1-2.")
            input("\nClick Enter to try again...")


def operators(name):
    pcls()
    print("\tHi, {name}. Welcome to Arithmetic Operators in Python")
    print("\nArithmetic Operators: +, -, *, /, //, %")
    print("\nINPUT: ")
    print("""numOne = eval(input("Enter a number: "))
numTwo = eval(input("Enter a number: "))

sum = numOne + numTwo
diff = numOne - numTwo
prod = numOne * numTwo
quot = numOne / numTwo
expo = numOne ** numTwo
rem = numOne % numTwo
fDiv = numOne // numTwo

print()
print("The sum of ", numOne, "and", numTwo, "is", sum)
print("The difference of ", numOne, "and", numTwo, "is", diff)
print("The product of ", numOne, "and", numTwo, "is", prod)
print("The quotient of ", numOne, "and", numTwo, "is", quot)
print(numOne, "exponent by ", numTwo, "is", expo)
print("The remainder of ", numOne, "and", numTwo, "is", rem)
print("The floor division of ", numOne, "and", numTwo, "is", fDiv)
print()""")
    print("\n\nOUTPUT: ")
    print("""\nEnter a number: 12
Enter a number: 15

The sum of  12 and 15 is 27
The difference of  12 and 15 is -3
The product of  12 and 15 is 180
The quotient of  12 and 15 is 0.8
12 exponent by  15 is 15407021574586368
The remainder of  12 and 15 is 12
The floor division of  12 and 15 is 0""")


def condition(name):
    while True:
        pcls()
        print(f"Hello, {name}! Welcome to Condition in Python")
        print("\n\tConditional Statements are statements in Python that provide a choice for the control flow based on a condition.")
        print("\nIt means that the control flow of the Python program will be decided based on the outcome of the condition.")

        print("\nMenu in Condition in Python")
        print("\n1). Conditional statement")
        print("2). Back to main menu")

        condition = input("\nEnter a number from 1-2: ")
        if condition == "1":
            print("\nConditional statement:")
            print("\nif \nelif \nelse \nnested")
        
        elif condition == "2":
            print("\nReturning to the Main Menu...")
        return


def poperators(name):
    while True:
        pcls()
        print(f"Hello, {name}! Welcome to Operator in Python.")
        print("\n\tOperators in general are used to perform operations on values and variables.")
        print("These are standard symbols used for logical and arithmetic operations.")

        print("\nMenu in Operator in Python: ")
        print("\n 1).Arithmetic Operators")
        print("\n 2).Comparison Operators")
        print("\n 3).Logical Operators")
        print("\n 4).Assignment Operators")
        print("\n 5).Back to Menu Operators...")
        print("\n===================================")
        

        operator = input("\nPick a number from 1-5: ")

        if operator == "1":
            print("\nInput:")
            print("""\tArithmetic Operators")""")
            print("\t+ \t- \t* \t/ \t// \t%")
            print("""
sum = uno + dos
difference = uno - dos
product = uno * dos
quotient = uno / dos
exponent = uno ** dos
remainder = uno & dos
floorDivision = uno // dos

print()
print("The sum of ", uno, "and", dos, "is", sum)
print("The difference of ", uno, "and", dos, "is", difference)
print("The product of ", uno, "and", dos, "is", product)
print("The quotient of ", uno, "and", dos, "is", quotient)
print(uno, "exponent by ", dos, "is", exponent)
print("The remainder of ", uno, "and", dos, "is", remainder)
print("The floor division of ", uno, "and", dos, "is", floorDivision)
print()""")
            
            print("\n\nOutput: ")

            print("""\nEnter a number: 8
Enter a number: 14

The sum of 8 and 14 is 22
The difference of 8 and 14 is -6
The product of 8 and 14 is 112
The quotient of 8 and 14 is 0.6
8 exponent by 14 is 4398046511104
The remainder of 8 and 14 is 8
The floor division of 8 and 14 is 0""")
        
        elif operator == "2":
            print("\nComparison Operators")
            print("\n")
            print("""\t\t== means Equal
                != Not equal
                >  Greater than
                <  Less than
                >= Greater than or equal
                <= Less than or equal""")
            
        elif operator == "3":
            print("Logical Operators")
            print("Input")
            print("""x=8
print(x > 8 and x < 14)""")
            print("Output")
            print("True")


            print("Input")
            print("""x=8
not(x < 5 and x < 10)""")
            print("Output")
            print("False")

        elif operator == "4":
            print("Assignment Operators")
            print("x = 14 \nx += 8 \nx -= 8 \nx *= 8 \nx /= 8 \nx %= 8 \nx //= 8 \nx **= 8")

        elif operator == "5":
            print("\nReturning to the Main Menu...")
            return


def function():
    while True:
        pcls()
        print("\nA function is a block of code which only runs when it is called.")
        print("\nYou can pass data, known as parameters, into a function.")
        print("A function can return data as a result.")

        print("\nMenu in Function in Python")
        print("1.) Create")
        print("2.) Call")
        print("3.) Back to main menu")

        function = input("\nEnter a number 1-3: ")
        if function == "1":
            print("\nCreate: ")
            print("\nInput")
            print("""def my_function():
  print("Hello, World""")
            print("\nOutput")
            print("Hello, World")

        elif function == "2":
            print("\nCall: ")
            print("\nInput")
            print("""def my_function():
  print("Hello from a function")

my_function()""")
            print("\nOutput")
            print("Hello, World")

        elif function == "3":
            print("\nReturning to the Main Menu...")
        return

    else:
        print("Invalid!")


def loops(name):
    while True:
        pcls()
        print(f"Hello, {name}! Welcome to Loops")
        print("\nA for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
        print("\nThis is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.")
        print("\nWith the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.")

        print("\nMenu in loops in Python")
        print("\n1.) For Loops")
        print("2.) while Loops")
        print("3.) Back to main menu")

        loops = input("\nEnter a number 1-3: ")
        if loops == "1":
             print("\nFor Loops:")
             print("\nInput")
             print("""\nnames = ["Ally", "Shella", "Gio"]
for x in names:
  print(x)""")
             print("\nOutput")
             print("\nAlly \nShella \nGio")
        
        elif loops == "2":
             print("\nwhile loop:")
             print("\nInput")
             print("""a = 1
while a < 8:
  print(a)
  a += 1")""")
        elif loops == "3":
             print("\nReturning to the Main Menu...")
        return
    

def list(name):
    while True:
        pcls()
        print(f"\nHello, {name}! Welcome to List")
        print("\nLists are used to store multiple items in a single variable.")
        print("Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.")

        print("\n\nMenu in List in Python")
        print("\n1.) Append")
        print("2.) Length")
        print("3.) Insert")
        print("4.) Back to main menu")

        list = input("\nEnter a number 1-4: ")
        if list == "1":
            print("\nAppend:")
            print("\nInput")
            print("""\na = [8, 16, 24, 32]
a.append(40)
print(a)""")
            print("\nOutput:")
            print("[8, 16, 24, 32, 40]")
        elif list == "2":
            print("Length:")
            print("Input")
            print("""a = [8, 16, 24, 32, 40]
length = len(a)
print(length)""")
            print("\nOutput")
            print("40")

        elif list == "3":
            print("Insert:")
            print("Input")
            print("""inschool = ["ADMU","UST","NU"]
inschool.insert(1,"UP")
print(inschool)""")
            print("\nOutput")
            print("['ADMU', 'UP', 'UST', 'NU']")

        elif list == "4":
            print("\nReturning to the Main Menu...")
        return


def exittt(name):
    print(f"\nThank you, {name}!")
    exittt()


def topmenu():
    pcls()
    name = input("Please enter your name: ")
    input(f"Good day, {name}!")
    goon = input("You what to start the program? (Yes or No): ")
    while True:
        if goon.lower() == "yes":
            print("Okay, Let's goo!")
            print("======================================================================")
            print("Top Menu")
            print("1.) Print Statement")
            print("2.) Variables")
            print("3.) Operators")
            print("4.) Condition")
            print("5.) Function")
            print("6.) Loops")
            print("7.) List")
            print("0.) Exit")

            print("======================================================================")
            pick = input("pick a number: ")

            if pick == "1":
                fstatement(name)

            elif pick == "2":
                Pvariables(name)

            elif pick == "3":
                poperators(name)

            elif pick == "4":
                condition(name)

            elif pick == "5":
                function(name)

            elif pick == "6":
                loops(name)

            elif pick == "7":
                list(name)

            elif pick == "0":
                exittt(name)

            else:
                print("Invalid Input. Please try again.")
                input("\nClick ENTER to try again.")

        else:
            print("Thank you. Have a great day ahead!")
            break 
    
topmenu()