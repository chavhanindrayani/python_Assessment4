Number = [12,23,45,56,67,88]
with open('e:\python\mydata.txt', 'w') as file:
    for num in Number:
        file.write('{Number}')
        
print("number write in mydata.txt")