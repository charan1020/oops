#exception is an event that is raised when an error occurs in the program.
#(zero division error, file not found error, etc.)
#we will do by these 1.try 2.except 3.finally 4.raise 5.assertion
try:
    number1 = int(input("Enter a number: "))
    print(1/number1)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:#here e is the instance of the Exception class
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")