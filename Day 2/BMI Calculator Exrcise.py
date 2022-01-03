
# Write A program  that calculate the body mass index (BMI) from a user weight and height
#  The BMI is measure of some  weight talking into account thair height  e.g  if a tall person both weight
#  the some Amount the short person is usually moreoverweight


#  The BMI  is calculated  by dividing  a person weight (in kg ) by the squire 
#  of thair height (in m) : 

height = input("Enter Your Height in m :")
weight = input("Enter Your Weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)