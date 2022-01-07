import random
# splite String method
name_str = input("Give me everybody,s Name , seperated ny a comma. ")
# 
names = name_str.split(",")
num_items = len(names)
random_choice = random.randint(0,num_items -1)
print(random_choice)