import random 
Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"

user_choice = input("what do you choose ? Type 0 for rock , 1 for paper and 2 for Scissors.")

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice == 0 and computer_choice  == 2 :
    print("User Win")
elif computer_choice  >user_choice:
 print("Computer Win !")