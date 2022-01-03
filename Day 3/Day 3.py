print("Welcome to the rollercoster")
height = int(input("what is your height in cm ? :"))
bill = 0
if height > 120:
    print ("you can ride the rollercoster")
    age = int(input("What is Your Age ?"))
    if age < 12:
     bill = 5 
     print ("child tickets are $5.")
    elif age <= 18:
     bill = 7  
     print("youth tickets are $7.")
         
    else:
     bill = 12
    print("adult tickets are $12.")

    wants_photo = input("DO you a photo Taken ? Y or No")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is $ {bill} ")
else:
    print("Sorry ,you have to go taller before you can ride .")

#     height = float(input("enter your Height in m :"))
#     weight = float(input("enter your weight in kg :"))
#     bmi = round(weight/height ** 2)
# if bmi < 18.5:
#     print (f" you are{bmi}under Weight ")
# elif bmi < 25:
#     print (f"your bmi is {bmi} you hav a normal weight . ")
# elif bmi > 25:
#     print (f" you Are OverWeight ")
# elif bmi < 30:
#     print (" Your Weight is {bmi} you are  Over Weight ")
# elif bmi > 30:
#     print (" obese ")
# elif bmi > 35:
#     print ("clinically obese")
# else:
#  print("please lose Your Weight")

 # =======================================================================
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
