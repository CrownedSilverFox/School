import json


students = json.load(open('Students.json'))
teachers = json.load(open('Teachers.json'))

#1.1
print([student["name"] for student in students])

#1.2
print([teacher["name"] for teacher in teachers])

#1.3
print([(student['name'], student['surname']) for student in students if student['class'] == '6 А'])

#1.4
print(list(set([teacher['school'] for teacher in teachers])))

#1.5
surnames = [student['surname'] for student in students]
for surname in list(set([student['surname'] for student in students])):
    surnames.remove(surname)
print([(student['name'], student[surname]) for student in students if student['surname'] in surnames])


#2.1
