# # players = {
# #     "Ali": [8, 7, 9, 6, 10],
# #     "Reza": [5, 6, 7, 5, 6],
# #     "Amir": [9, 9, 8, 10, 9],
# #     "Mehdi": [4, 5, 6, 4, 5],
# #     "Sara": [7, 8, 8, 9, 7]
# # }
# # best_score = 0
# # best_player = ""
# # for player in players:
# #     total=0
# #     average=0
# #     # print (player)
# #     for number in players[player]:
# #     #  print (player,number)
# #      total=total+number
# #     average=total/len(players[player])
# #     if total > best_score:
# #      best_score = total
   
# #      best_player = player
# #     print(player,total)
# #     print(average)
# # print(best_player,best_score)
# best_player=0
# best_socer=''

# t={
#     'ali':[10,20,30],
#     'amir':[3,16,15]
# }
# for i in t:
#     total=0
#     random=0
#     # print(i)
#     for number in t[i]:
#      total=total+number
#      random=total/len(t[i])
#     print(max(t[i]))

    
#     # print(i,total)
#     # print(random)
#     if random > best_player:
#        best_player=total
#        best_socer=i
#        print(best_player,best_socer)

# def add(a, b):
#     result = a + b
#     m=result/2
#     return m

# x = add(133, 20)
# print(x)
       

# def calculate_total(scores):
#     total = 0

#     for score in scores:
#         total = total + score

#     return total


# numbers =[12,25,14,18]

# result = calculate_total(numbers)

# print(result)
# def pejman(ali):
#     total=0
#     for name in ali:
#         total=total+name
#     return total
# numbers=[12,25,4,7,7]
# ahmadi=pejman(numbers)
# print(ahmadi)
# def iran (tehran):
#     fe=0
#     for pa in tehran:
#      fe=fe+pa
#      avreage=fe/ len(tehran)
     
#     return avreage
# number=[12,13,14,52]
# ahmadi=iran(number)
# print(ahmadi)

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

        





        
     

    
            
   

