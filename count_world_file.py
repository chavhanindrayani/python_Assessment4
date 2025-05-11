filename = "e:\python\example.txt.txt"
def is_count_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            count = len(words)
            return count
    except FileNotFoundError:
        print("File Not Found Error {filename} :")
        return 0

result = is_count_word(filename)
print(f"result {result}")

        
    
        
