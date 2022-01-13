import random 
Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"

user_choice = int(input("what do you choose ? Type 0 for rock , 1 for paper and 2 for Scissors. \n"))

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice  == 2 :
    print("User Win")
elif computer_choice > user_choice:
  print("It`s  a draw")      
elif computer_choice  >user_choice:
 print("You Win !")
else:
 print("You type an invalid number , you lose ! ")