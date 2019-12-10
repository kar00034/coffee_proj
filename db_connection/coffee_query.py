from mysql.connector import Error
from db_connection.db_connection import ConnectionPool


def insert_products(sql, products):  # 여러 행
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print('Error:', e)
    finally:
        cursor.close()
        conn.close()


def insert_sale(sql, products):  # 여러 행
    try:
        conn = ConnectionPool.get_instance().get_connection()
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print('Error:', e)
    finally:
        cursor.close()
        conn.close()
