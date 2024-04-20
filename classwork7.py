#lambda
#
# def up_letter(word: str):
#     return word.title()
#
# def show_words(func,words):
#     for i in words:
#         print(func(i))
#
#
#
# show_words(lambda word: word.title(), ['sezim','muras','said'])
#
#
# cities = ['london','paris','barcelona']
# show_words(up_letter,cities)


# filter, map, sorted

# students = ['said','sezim','elmira','muras','azamat','aidai','bekmuraz','sherbol','nurgazy','faris','roman']
#
# students_sorted = sorted(students, key=lambda name: name[-1])
# print(students_sorted)

# mapped_students = tuple(map(lambda name: name.upper(), students))
# print(mapped_students)

# students_filtered = list(filter(lambda name: len(name) == 5, students))
# students_filtered = list(filter(lambda name: 'n' in name, students))
#
# print(students_filtered)


#Работа с исключениями


#обработка исключений

# try:
#     code
# except:
#     code
#     message
# finally:
#     code




