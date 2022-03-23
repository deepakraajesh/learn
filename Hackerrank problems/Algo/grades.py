def gradingStudents(grades):
    res=[]
    for i in grades:
        if(i<38):
            res.append(i)
        else:
            j=i%5
            if(j==3):
                i+=2
                res.append(i)
            elif(j==4):
                i+=1
                res.append(i)
            else:
                res.append(i)
    print(*res,end=' ')

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    gradingStudents(grades)