#5.File Reading with Try-Except:
#Write a Python program that reads a file data.txt and handles any exceptions (e.g., FileNotFoundError, PermissionError) that may occur during file reading.
filename = "e:\python\greeting.txt"
try:
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
        
except FileNotFoundError:
    print("Error : 'fiel.txt' was not found.")
except PermissionError:
    print("Error: You do not have permission to read 'data.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    