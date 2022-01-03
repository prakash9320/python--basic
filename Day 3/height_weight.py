height = float(input("enter your Height in m :"))
weight = float(input("enter your weight in kg :"))
bmi = round(weight/height ** 2)
if bmi < 18.5:
    print (f" you are{bmi}under Weight ")
elif bmi < 25:
    print (f"your bmi is {bmi} you hav a normal weight . ")
elif bmi > 25:
    print (f" you Are OverWeight ")
elif bmi < 30:
    print (" Your Weight is {bmi} you are  Over Weight ")
elif bmi > 30:
    print (" obese ")
elif bmi > 35:
    print ("clinically obese")
else:
 print("please lose Your Weight")
