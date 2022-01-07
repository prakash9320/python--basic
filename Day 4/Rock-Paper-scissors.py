import random 
Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"

user_choice = input("what do you choose ? Type 0 for rock , 1 for paper and 2 for Scissors.")

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")