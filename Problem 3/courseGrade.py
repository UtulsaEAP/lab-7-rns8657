def courseGrade(name):
    info = open(name, 'r')
    students = info.readlines()
    class_exam_one = []
    class_exam_two = []
    class_exam_three = []
    for i in range (len(students)):
        student_info = students[i].split()
        average_exam = (int(student_info[2]) + int(student_info[3]) + int(student_info[4])) / 3
        if (average_exam >= 90):
            grade = "A"
        elif(average_exam >= 80):
            grade = "B"
        elif(average_exam >= 70):
            grade = "C"
        elif(average_exam >= 60):
            grade = "D"
        else: 
            grade = "F"
        last_name = student_info[0]
        first_name = student_info[1] 
        class_exam_one.append(int(student_info[2]))
        class_exam_two.append(int(student_info[3]))
        class_exam_three.append(int(student_info[4]))
        if(name == "./Problem 3/StudentInfo.tsv" ):
            #open("./Problem 3/report.txt", 'w').close()
            report = open("./Problem 3/report.txt", '+a')
        elif(name == "./Problem 3/StudentInfo1.tsv"):
            #open("./Problem 3/report1.txt").close()
            report = open("./Problem 3/report1.txt", '+a')
        elif(name == "./Problem 3/StudentInfo2.tsv" ):
            #open("./Problem 3/report2.txt").close()
            report = open("./Problem 3/report2.txt", '+a')
        report.write(last_name + "\t" + first_name + "\t" + str(student_info[2]) + "\t" + str(student_info[3]) + "\t" + str(student_info[4]) + "\t" + grade + "\n")
    class_avg_one = sum(class_exam_one) / len(class_exam_one)
    class_avg_two = sum(class_exam_two) / len(class_exam_two)
    class_avg_three = sum(class_exam_three) / len(class_exam_three)
    report.write("Averages: midterm1 " + str(class_avg_one) + ", midterm2 " + str(class_avg_two) + ", final " + str(class_avg_three))
    
    report.close()
    


if __name__ == "__main__":
    name = "./Problem 3/" + str(input())
    courseGrade(name)
    courseGrade("./Problem 3/StudentInfo1.tsv")
    courseGrade("./Problem 3/StudentInfo2.tsv")
    
    
    