#  Write a program that  add  digit  in  a 2 gidit number 
#  e.g if the  input  was 35 the the otput should be 3 +5 = 8
 
  # 
two_digit_number = input("Type a two digit number : ") 

 # check the data type of two_digit_number
print(type(two_digit_number))
 
 # get the first and second digit using subscripting then convert String into int
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
  
   # add the Two Digit Together
result = int(first_digit) + int(second_digit)
print(result)