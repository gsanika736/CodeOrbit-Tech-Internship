
# ==================================
# SIMPLE CALCULATOR
# ==================================

# Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Displaying arithmetic operations
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Taking the operator from the user
    choice = input("Enter your choice (1-4): ")

    # Performing the selected operation
    if choice == "1":
        result = num1 + num2
        print("Addition Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Subtraction Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Multiplication Result:", result)

    elif choice == "4":
        # Checking division by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
        print("Division Result:", result)

    else:
        print("Invalid choice! Please select between 1 and 4.")

# Handling division by zero errors
except ZeroDivisionError as e:
    print("Error:", e)

# Handling invalid numerical inputs
except ValueError:
    print("Invalid input! Please enter valid numbers.")

# Displaying a final message
finally:
    print("Thank you for using Simple Calculator!")
