# key:value словарь-dict
# ключи не должны повторяться
# неизменяемые типы данных могут быть ключом:
 student = {'age':21,'height':1.77,'is_married': False,'hobby': ['chess','books','english'],'education':('school','college')}
 print(student.get('hoby'))
 print(student['hobby'])

 for i in student:
     print (f'{i}: {student[i]}')
print(student)
 print(student['name'])
 print(student['age'])



# numbers = (1, 2, 3, 2, 4, 1, 5, 3)
# numberz = {1, 2, 3, 2, 4, 1, 5, 3}
# print (numbers)
# print (numberz)
# print (type(numberz))   #set


