import os
import pymysql

from dotenv import load_dotenv


load_dotenv()

def get_connection():
    return pymysql.connect(
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        user=os.getenv("USER"),
        password=os.getenv("PASS"),
        database=os.getenv("DB"),
        cursorclass=pymysql.cursors.DictCursor
    )


def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT 1")
        print(" Connected and query worked")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f" Connection failed: {e}")



def show_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("Tables:")
    for t in tables:
        print(t)

    cursor.close()
    conn.close()
