import sqlite3


conn = sqlite3.connect('hw8.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL)''')


cursor.execute('''INSERT INTO countries (title) VALUES ('Киргизия')''')
cursor.execute('''INSERT INTO countries (title) VALUES ('Германия')''')
cursor.execute('''INSERT INTO countries (title) VALUES ('Китай')''')


cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  area REAL DEFAULT 0,
                  country_id INTEGER,
                  FOREIGN KEY (country_id) REFERENCES countries(id))''')


cursor.execute('''INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 123.45, 1)''')
cursor.execute('''INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 456.78, 2)''')
cursor.execute('''INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 789.01, 3)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS students
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  city_id INTEGER,
                  FOREIGN KEY (city_id) REFERENCES cities(id))''')


cursor.execute('''INSERT INTO students (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)''')
cursor.execute('''INSERT INTO students (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 2)''')
cursor.execute('''INSERT INTO students (first_name, last_name, city_id) VALUES ('Мария', 'Сидорова', 3)''')



def select_city():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT title FROM cities''')
    cities = cursor.fetchall()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city[0]}")

    city_id = int(input("Введите id города: "))
    conn.close()

    return city_id



def display_students(city_id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                      FROM students
                      JOIN cities ON students.city_id = cities.id
                      JOIN countries ON cities.country_id = countries.id
                      WHERE cities.id = ?''', (city_id,))

    students = cursor.fetchall()
    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    else:
        print("В выбранном городе нет учеников")

    conn.close()



while True:
    city_id = select_city()

    if city_id == 0:
        break

    display_students(city_id)