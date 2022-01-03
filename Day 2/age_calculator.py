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