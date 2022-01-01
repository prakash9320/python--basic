print("Welcome to the rollercoster")
height = int(input("what is your height in cm ? :"))
if height > 120:
    print ("you can ride the rollercoster")
    age = int(input("What is Your Age ?"))
    if age < 12:
        print ("please pay $5.")
    elif age <= 18:
     print("please pay $7.")
    elif age < 22:
        print ("")
    else:
       print("please pay $12.")
else:
    print("Sorry ,you have to go taller before you can ride .")

    height = float(input("enter your Height in m :"))
    weight = float(input("enter your weight in kg :"))
    bmi = round(weight/height ** 2)
if bmi < 18.5:
    print (f" you are{bmi}under Weight ")
elif bmi < 25:
    print (f"Normal weight ")
elif bmi > 25:
    print (f" you Are OverWeight ")
elif bmi < 30:
    print (" Your Weight is under 30 but is Over Weight ")
elif bmi > 30:
    print (" obese ")
elif bmi > 35:
    print ("clinically obese")
else:
 print("please lose Your Weight")