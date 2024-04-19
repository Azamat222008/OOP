import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(connection, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES
    (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_quantity(connection, product):
    sql = '''UPDATE products SET quantity = ?
                    Where id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(connection, product):
    sql = '''UPDATE products SET price = ?
                    Where id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(connection,id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)





def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)
def select_products_by_limit(connection, limit_one,limit_two):
    sql = '''SELECT * FROM products WHERE price < ? AND quantity < ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (limit_one,limit_two))
        rows_list = cursor.fetchall()


        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_product_by_word(connection, word):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, ('%' + word + '%',))
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)



sql_table_db = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)'''

my_conn = create_connection('HW.db')
if my_conn is not None:
    print('Connected to db')
    create_table(my_conn, sql_table_db)

    insert_product(my_conn, ('мыло хозяйственное', 40.5, 200))
    insert_product(my_conn, ('мыло туалетное', 55.0, 100))
    insert_product(my_conn, ('мыло детское', 80.0, 155))
    insert_product(my_conn, ('жидкое мыло с запахом ванили', 120.0, 38))
    insert_product(my_conn, ('порошок автомат', 120.0, 84))
    insert_product(my_conn, ('порошок ручная стирка', 96.54, 49))
    insert_product(my_conn, ('шампунь детский Три кота', 180.55, 3))
    insert_product(my_conn, ('мужской шампунь Clear', 280.0, 24))
    insert_product(my_conn, ('женский шампунь PRO', 345.09, 55))
    insert_product(my_conn, ('зубная паста', 130.6, 8))
    insert_product(my_conn, ('средство для мытья посуды', 180.0, 15))
    insert_product(my_conn, ('чистящее средство', 85.3, 4))
    insert_product(my_conn, ('туалетная бумага', 14.7, 670))
    insert_product(my_conn, ('бумажные салфетки', 20.8, 560))
    insert_product(my_conn, ('влажные салфетки', 85.0, 3))
    update_product_quantity(my_conn,(70, 2))
    update_product_price(my_conn,(370.09,9))
    delete_product(my_conn, 13)
    select_all_products(my_conn)
    select_products_by_limit(my_conn, 100, 5)
    select_product_by_word(my_conn,'мыло')
    my_conn.close()







