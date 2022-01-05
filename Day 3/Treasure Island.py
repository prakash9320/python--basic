print("Welcome to Tresure Island")
print("Your mission is to find the treasure")
choice1 = input('you `re at the crossroad , where do you want to go ? Type "left" or "right". \n').lower()

if choice1 == "left":
    # continue in the game
 choice2 = input('You`ve come to lake . There is an island in the middle of the lake. Type "wait" to wait for  a boat .Type "swim" to swim across .')
 if choice2 == "wait":
   # Game Will Be continue
    choice3 = input("You Arrive  at the island unharmed  . There is a house  with 3 doors . One Yellow and One Blue Which color do you choose ?").lower()
    if choice3 =="red":
      print("Its`s a room  full of fire . Game Over .")
    elif choice3 =="yellow":
      print("You Found the Tresure ! You Win ")
    elif choice3 =="blue":
      print("You Enter The Room  of beast . Game Over")
      
 else:
  print("You Get Attacked by an angry Trout . Game Over .")
else:
  print("You fell into a hole.Game Over") 