student_score = input("Input  a List of student score").split()
for n in range(0,len(student_score)) :
    student_score[n] = int(student_score[n])
    print(student_score)

    print(max(student_score))   

    highest_Score = 0
    for score in student_score :
        if score > highest_Score:
            highest_Score = score
    print(f"The highest score in the class is : {highest_Score}")        