
def calculate_average(scores):
    total = 0

    for score in scores:
        total=total+score

    average = total/len(scores)

    return average

students = {
    "Ali": [15, 18, 12, 20],
    "Reza": [8, 9, 12, 7],
    "Sara": [19, 20, 18, 19],
    "Amir": [10, 14, 13, 11],
    "Mehdi": [5, 8, 6, 9]
}
while True:
    m=input("""
        1. Show all students
        2. Calculate averages
        3. Check student status
        4. Find best student
        5. Add new student
        6. Search student
        7. Exit

       Choose an option: _
   """ )
    if m=='1':
        for student in students:
            print(student, students[student])
    elif m== '7':
        print("Goodbye!")
        break
    elif m=='2':
      for student in students:
         number=students[student]
         a=calculate_average(number)
         print(student,':',a)
    elif m=='3':
        for student in students:
            number=students[student]
            a=calculate_average(number)
            if a >=17:
                print(student,':','Excellent')
            elif a >=10:
                print(student,':','pass')
            else:
                print(student,':','fail')
    elif m=='4':
        best_student = ""
        best_average = 0
        for student in students:
            number=students[student]
            a=calculate_average(number)
            if a > best_average:
                best_average=a
                best_student=student
        print(best_student,best_average)
    elif m=='5':
        name=input('please enter student name?')
        if name in students:
            print("Student already exists!")
        else:
           scores=[]
           for i in range(4):
               score=int(input('please enter score?'))
               scores.append(score)
           students[name]=scores
           print("Student added successfully!")
    elif m=='6':
        serch=input('please enter the name?')
        if serch in students:
                   print('Student found!')
                   print(serch, students[serch])
        else:
                print('student not fond')

        





        
     

    
            
   

