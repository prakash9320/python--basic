print("Welcom to the love calculator")
name1 = input("What is Your Name\n")
name2 = input("What is thair name\n")
combine_string = name1 +name2
lower_case_string = combine_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
 # change the type String to int 
love_score = int(str(true) + str(love))

if (love_score <10) or (love_score > 90) :
    print(f"Your Love Score is {love_score} , you go to together like coke and  mentos ")
elif(love_score >=40 or love_score <= 50):
    print(f"Your score is {love_score} , you are alright together")
else :
    print(f"your score is {love_score}") 