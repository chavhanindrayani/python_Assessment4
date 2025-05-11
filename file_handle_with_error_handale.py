#2.	File Handling with Error Handling:
#Write a Python program to read a file data.txt. Use exception handling to handle cases where the file does not exist or cannot be opened.
filename = "e:\python\greetting.txt"
try:
    with open(filename, 'r') as f:
        data = f.read()
        print(f"File Content:{data}")
        
except FileNotFoundError:
    print("Error: The file 'greeting.txt' was not found.")
    
except IOError:
    print("Error: The file could not be opened or read.")