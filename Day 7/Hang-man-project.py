import random
work_list = ["ardvark","baboon","camel"]

# TODO-1 randomely choose a word from word_list and assign 
#  it to variable  called chosem_word
     

chosen_word = random.choice(work_list)
 # Testing Code
print("pas st , the solution  is :"+ chosen_word)

# TODO-2 Aske the user to guess the letter and assign thair
#      answer to variable called guess .Make guess 
#      lowercase 

display = []
for _ in range(len(chosen_word)):
   display += "_"
   print(display)
guess = input("Enter a word")
print(guess)
# TODO-3 CHECK IF THE LATTER THE USER GUESSESD  (GUESSE)
#  IS ONE OF THE LETTER  IN THE CHOOSE_WORD
for letter in work_list:
    if letter == guess:
       print("Right")
    else:
       print("Wrong")  