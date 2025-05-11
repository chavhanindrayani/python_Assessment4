#4.Try-Except-Else-Finally:
#Write a Python program that takes two integers as input and divides them. Use a try-except-else-finally block to handle division by zero and print appropriate messages.
def number_divides():
    try:
        num1 = int(input("Enetr the 1 number :"))
        num2 = int(input("Enetr the 1 number :"))
        result = num1/num2
        print(f"result {result}")
        
    except ZeroDivisionError:
        print("Error : connot divide by zero")
    except ValueError:
        print("Error : please enetr valid integers.")
    else:
        print(f"Result : {num1} / {num2} = {result}")
    finally:
        print("Execution complete. Thank you for using the program.")
        
    
number_divides()