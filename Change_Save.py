import json


def get_index(data, f_name):
    for human in data:
        if f_name.replace(' ', '') == (human['name']+human['middle_name']+human['surname']):
            return data.index(human)


def get_last_id(data):
    id_list = [int(human['id']) for human in data]
    return max(id_list)


with open('Students_id.json') as data_file:
    students = json.load(data_file)
with open('Teachers_id.json') as data_file:
    teachers = json.load(data_file)
students.append({
    "name": "Георгий", "middle_name": "Александрович",
    "surname": "Масляков", "school": "67 школа", "class": "10 А", "birth_day": "12.07.1993",
    'id': get_last_id(students)+1})
students.append({
    "name": "Константин", "middle_name": "Юриевич",
    "surname": "Поляков", "school": "72 гимназия", "class": "9 Б", "birth_day": "15.10.1994",
    'id': get_last_id(students)+1})
students.append({
    "name": "Алексей", "middle_name": "Васильевич",
    "surname": "Анчарский", "school": "67 школа", "class": "10 А", "birth_day": "01.01.1993",
    'id': get_last_id(students)+1})
students.append({
    "name": "Анна", "middle_name": "Сергеевна",
    "surname": "Анчарская", "school": "72 гимназия", "class": "8 В", "birth_day": "10.11.1995",
    'id': get_last_id(students)+1})
students.append({
    "name": "Виктор", "middle_name": "Викторович",
    "surname": "Викторов", "school": "67 школа", "class": "4 А", "birth_day": "19.09.1999",
    'id': get_last_id(students)+1})

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
    "birth_day": "02.09.1950",
    'id': get_last_id(teachers)+1
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
    "birth_day": "02.09.1950",
    'id': get_last_id(teachers)+1
  })

tchr_append_class = 'Ирина Владимировна Турцева'
class_append = '10 А'
teachers[get_index(teachers, tchr_append_class)]['class'].append(class_append)

std_del = 'Виктор Викторович Викторов'
students.pop(get_index(students, std_del))

class_del = '10 А'
students = [student for student in students if student['class'] != class_del]

tchr_del = 'Алексей Алексеевич Козлов'
teachers.pop(get_index(teachers, tchr_del))

school_del = '72 гимназия'
teachers = [teacher for teacher in teachers if teacher['school'] != school_del]

class_del_list = ['5 Б', '6 Б']
teacher_classes_del = 'Александр Сергеевич Черный'
teacher_index = get_index(teachers, teacher_classes_del)
for class_del in class_del_list:
    teachers[teacher_index]['class'].remove(class_del)

with open('Students_id.json', 'w') as data_file:
    data_file.write(json.dumps(students, ensure_ascii=False))
with open('Teachers_id.json', 'w') as data_file:
    data_file.write(json.dumps(teachers, ensure_ascii=False))