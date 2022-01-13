# Password Generator Project
import random
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n' ,'o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'   ]
number = ['0','1','2','3','4','5','6','7','8','9']

symbol = ['!','#','$','%','&','(',')','*','+']
 
print("Welcome to the pyPassword Generator !")
nr_letters = int(input("how many letters would you like in your password :\n"))
nr_symbol = int(input("How Many Symbol Would You  Like : \n"))
nr_number = int(input("How Many Number Would You Like :\n"))

# Eazy Level
password_list = []

for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letter))


for char in range(1,nr_symbol + 1):
 password_list +=random.choice(symbol)
 

for char in range(1,nr_number):
 password_list += random.choice(number)

print(password_list) 
random.shuffle(password_list)
print(password_list)



password = ""
for char in password_list:
 password += char
print('Your Password is :'+password)