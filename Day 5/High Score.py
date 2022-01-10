student_score = input("Input  a List of student score").split()
for n in range(0,len(student_score)) :
    student_score[n] = int(student_score[n])
    print(student_score)