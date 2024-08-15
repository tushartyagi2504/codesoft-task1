def main():
    print("Welcome to the Simple Calculator!")  
    
    # Show the options for operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the user's choice
    operation = input("Enter the number corresponding to the operation: ")

    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))  
    
    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"\nThe result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nThe result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nThe result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe result of {num1} / {num2} is: {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
