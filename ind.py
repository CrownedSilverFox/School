import json


def check(human, values):
    for key in values.keys():
        if (values[key] == human[key]) or (values[key] in human[key]):
            return True


def get_id_list(data, **kwargs):
    if 'class_room' in kwargs.keys():
        kwargs['class'] = kwargs.pop('class_room')
    return [human['id'] for human in data if check(human, kwargs)]


with open('Students_id.json') as data_file:
    students = json.load(data_file)
with open('Teachers_id.json') as data_file:
    teachers = json.load(data_file)

#2
surname_find = 'Иванов'
sur_id_list = [student['id'] for student in students if student['surname'] == surname_find]
print(['%s %s %s' % (student['surname'], student['name'], student['middle_name']) for student in students
       if student['id'] in sur_id_list])

#3
print(get_id_list(teachers, class_room='7 В'))
