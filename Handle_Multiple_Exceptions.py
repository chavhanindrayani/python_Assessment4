
#3.Handle Multiple Exceptions:
#Write a Python program that attempts to convert a user input to an integer. Handle both ValueError and ZeroDivisionError exceptions gracefully.
def Handle_Multiple_Exception():
    try:
        user_input = (input("Enetr the number :"))
        number = int(user_input)
        result = 100 / number
        print(f"result of 100 divided by number {number} is {result}")
        
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
Handle_Multiple_Exception()
    