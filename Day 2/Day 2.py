# Tupe Conversion 

# num_char = len(input("What Is Your Name"))
# new_num_char = str(num_char)
# print("Your Name is "+new_num_char+" Charactor")

# =====================================================

# Write a program that  add  digit  in  a 2 gidit number 
#  e.g if the  input  was 35 the the otput should be 3 +5 = 8
 
  # 
# two_digit_number = input("Type a two digit number : ") 

#  # check the data type of two_digit_number
# print(type(two_digit_number))
 
#  # get the first and second digit using subscripting then convert String into int
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
  
#    # add the Two Digit Together
# result = int(first_digit) + int(second_digit)
# print(result)


# ==================================BMI Calculator Exrcise ============================================

# Write A program  that calculate the body mass index (BMI) from a user weight and height
#  The BMI is measure of some  weight talking into account thair height  e.g  if a tall person both weight
#  the some Amount the short person is usually moreoverweight


#  The BMI  is calculated  by dividing  a person weight (in kg ) by the squire 
#  of thair height (in m) : 

# height = input("Enter Your Height in m :")
# weight = input("Enter Your Weight in kg: ")

# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)


# =================================================================================
#   Create a program using maths  and f-String that tell us how many days 
#   week ,month we have left time we actually have

age = input("What is Your Current Age")

age_as_int = int(age)
year_remaining = 90 -age_as_int
day_remaining = 365 * 365
week_remaining =  year_remaining * 52
month_remaining = year_remaining * 12

messege =  f"You Have {day_remaining} day , {week_remaining}  week and {month_remaining} month left"
print(messege)