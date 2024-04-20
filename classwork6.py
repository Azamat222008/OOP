# функции ,аргументы,* args **kwargs
# функция - def

# def get_square(length, width):
#     square = length * width
#     return square


# square_1 = get_square(5,5)
# square_victory = get_square(550, 150)
# print(square_1)
# print(square_victory)


# length = 5
# width = 5
# square_1 = length * width
# print(square_1)
 #
 # length = 550
 # width = 150
 # square_victory = length * width
 # print(square_victory)


# схема функции
# определение наименования(параметры):
#     тело функции
#     возвращение результата
#
# вызов функции
# наименования(аргументы)

# words = ['tokmok', 'karakol','kant']
# print(len(words))





#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#         return counter
#
# print(len1(words))

# def plus(*args):
#     return sum(args)
#
# print(plus(2,4,5,8))
# print(plus(223,4,5,834,45))



def menu(**kwargs):
    return kwargs

monday = menu()






# def get_data(name, surname ='неизвестно'):   #required positional parameter
#     print(f'name :{name} surname: {surname}')
#
# get_data('Mike' , "Tyson") #required positional argument
# get_data('Tom' , 'Maguire')
# get_data(surname='Пушкин', name='Алексанр')
# get_data('lev', 'tolstoy')