# fot loop in range 

# for number in range(1,11,3):
#  print(number)    


# ============

# total = 0
# for number in range(1,101):
#     total += number
#     print(total)

# =======================
 # exrcise
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0 :
      print("FizzBuss ")
    elif number % 3 == 0 :
     print("FizzBuzz")
    elif number % 5 == 5:
     print("FizzBuzz") 
    else :
        print(number) 