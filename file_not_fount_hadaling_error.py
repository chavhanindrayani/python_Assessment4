filename = "text.txt"
try:
    with open(filename,'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"Error: File Not Found The Erro {filename} ")
    
   # print(f"Error: the file {filename} not found")