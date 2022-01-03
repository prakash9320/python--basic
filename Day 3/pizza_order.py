print("Welcome to the  pizza  Deliveries")
size = input("what is pizza  do you  want S ,M , OR L")
add_pepperies = input(" Do you Want pepperies ?")
extra_cheese = input("Do you want Extra Cheese")
bill = 0
if size == 'S':
 bill += 15
elif size == 'M':
 bill += 20
elif size == 'L' :
 bill  += 25

if add_pepperies == "Y":
 if size == "S":
  bill +=2

if extra_cheese == "Y":
 bill += 1
else:
 bill += 3
print(f"Your bill is ${bill}")