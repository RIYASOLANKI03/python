import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']

print("welcome to the password generator")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_symbols=int(input(f"how many symbols would you likr?\n"))
nr_numbers=int(input(f"how many numbers would you like?\n"))

#easy
password=" " 


for char in range(0,nr_letters):
    password+=random.choice(letters)

for char in range(0,nr_symbols):
    password+=random.choice(symbols)

for char in range(0,nr_numbers):
    password+=random.choice(numbers)

print(password)

#hard
 
password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)