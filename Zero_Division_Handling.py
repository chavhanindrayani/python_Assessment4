#1.	Zero Division Handling:
#Write a Python program that takes two integers as input and divides them. Handle the ZeroDivisionError if the denominator is zero.
def divide_numbers():
    try:
        numerator = int(input("Enter the 1 Number : "))
        denominator = int(input("Enetr the 2 Number : "))
        result = numerator / denominator
        print(f"Result : {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integers.")
     
divide_numbers() # Run the function
 