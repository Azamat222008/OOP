mentors = ["кубаныч", "мирлан", "гулина", "камиля"]

while True:
    print("\nВыберите одну из следующих команд:")
    print("1) Добавление")
    print("2) Изменение")
    print("3) Удаление по индексу")
    print("4) Удаление по имени")
    print("0) Выход")

    choice = input("Введите номер команды: ")

    if choice == "1":
        if len(mentors) & lt; 10:
            name = input("Введите имя ментора: ")
            name = name.capitalize()
            if len(name) & lt;= 15:
                if name not in mentors:
                    mentors.append(name)
                    print("Имя успешно добавлено")
                else:
                    print("Такое имя уже существует в списке")
            else:
                print("Имя должно содержать не более 15 букв")
        else:
            print("Список менторов уже заполнен")

    elif choice == "2":
        old_name = input("Введите имя заменяемого ментора: ")
        new_name = input("Введите новое имя ментора: ")
        if old_name in mentors:
            if new_name not in mentors:
                new_name = new_name.capitalize()
                if len(new_name) & lt;= 15:
                    index = mentors.index(old_name)
                    mentors[index] = new_name
                    print("Имя успешно изменено")
                else:
                    print("Имя должно содержать не более 15 букв")
            else:
                print("Такое имя уже существует в списке")
        else:
            print("Введенного имени не существует в списке")

    elif choice == "3":
        index = int(input("Введите индекс удаляемого ментора: "))
        if index & lt; len(mentors):
            del mentors[index]
            print("Ментор успешно удален")
        else:
            print("Введенный индекс выходит за пределы списка")

    elif choice == "4":
        name = input("Введите имя удаляемого ментора: ")
        if name in mentors:
            mentors.remove(name)
            print("Ментор успешно удален")
        else:
            print("Введенного имени не существует в списке")

    elif choice == "0":
        break

    else:
        print("Неверный ввод, попробуйте снова")

mentors = tuple(mentors)
print("Список менторов:", mentors)