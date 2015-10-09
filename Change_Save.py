import json


def get_index(data, f_name):
    for human in data:
        if f_name.replace(' ', '') == (human['name']+human['middle_name']+human['surname']):
            return data.index(human)

students = json.load(open('Students.json'))
students.append({
    "name": "Георгий", "middle_name": "Александрович",
    "surname": "Масляков", "school": "67 школа", "class": "10 А", "birth_day": "12.07.1993"})
students.append({
    "name": "Константин", "middle_name": "Юриевич",
    "surname": "Поляков", "school": "72 гимназия", "class": "9 Б", "birth_day": "15.10.1994"})
students.append({
    "name": "Алексей", "middle_name": "Васильевич",
    "surname": "Анчарский", "school": "67 школа", "class": "10 А", "birth_day": "01.01.1993"})
students.append({
    "name": "Анна", "middle_name": "Сергеевна",
    "surname": "Анчарская", "school": "72 гимназия", "class": "8 В", "birth_day": "10.11.1995"})
students.append({
    "name": "Виктор", "middle_name": "Викторович",
    "surname": "Викторов", "school": "67 школа", "class": "4 А", "birth_day": "19.09.1999"})

std_fl = open('Students.json', 'w')
std_fl.write(json.dumps(students, ensure_ascii=False))
std_fl.close()

teachers = json.load(open('Teachers.json'))
teachers.append({
    "name": "Ирина",
    "middle_name": "Владимировна",
    "surname": "Турцева",
    "school": "67 школа",
    "class": [
      "1 А",
      "4 Б",
      "10 А"
    ],
    "birth_day": "02.09.1950"
  })
teachers.append({
    "name": "Алексей",
    "middle_name": "Алексеевич",
    "surname": "Козлов",
    "school": "72 гимназия",
    "class": [
      "1 А",
      "4 Б",
      "10 А"
    ],
    "birth_day": "02.09.1950"
  })

tchr_fl = open('Teachers.json', 'w')
tchr_fl.write(json.dumps(teachers, ensure_ascii=False))
tchr_fl.close()

tchr_append_class = 'Ирина Владимировна Турцева'
class_append = '10 А'
teachers = json.load(open('Teachers.json'))
teachers[get_index(teachers, tchr_append_class)]['class'].append(class_append)
tchr_fl = open('Teachers.json', 'w')
tchr_fl.write(json.dumps(teachers, ensure_ascii=False))
tchr_fl.close()

std_del = 'Виктор Викторович Викторов'
students = json.load(open('Students.json'))
students.pop(get_index(students, std_del))
std_fl = open('Students.json', 'w')
std_fl.write(json.dumps(students, ensure_ascii=False))
std_fl.close()

class_del = '10 А'
students = json.load(open('Students.json'))
students = [student for student in students if student['class'] != class_del]
std_fl = open('Students.json', 'w')
std_fl.write(json.dumps(students, ensure_ascii=False))
std_fl.close()

tchr_del = 'Алексей Алексеевич Козлов'
teachers = json.load(open('Teachers.json'))
teachers.pop(get_index(teachers, tchr_del))
tchr_fl = open('Teachers.json', 'w')
tchr_fl.write(json.dumps(teachers, ensure_ascii=False))
tchr_fl.close()

school_del = '72 гимназия'
teachers = json.load(open('Teachers.json'))
teachers = [teacher for teacher in teachers if teacher['school'] != school_del]
std_fl = open('Students.json', 'w')
std_fl.write(json.dumps(students, ensure_ascii=False))
std_fl.close()

class_del_list = ['6 Б', '6 Г']
teacher_classes_del = 'Владимир Сергеевич Вышкин'
teachers = json.load(open('Teachers.json'))
teacher_index = get_index(teachers, teacher_classes_del)
for class_del in class_del_list:
    teachers[teacher_index]['class'].remove(class_del)
tchr_fl = open('Teachers.json', 'w')
tchr_fl.write(json.dumps(teachers, ensure_ascii=False))
tchr_fl.close()