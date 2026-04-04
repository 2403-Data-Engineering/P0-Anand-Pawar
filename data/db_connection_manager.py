import os
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT")),
        user=os.getenv("USER"),
        password=os.getenv("PASS"),
        database=os.getenv("DB")
    )

def select_messages() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary = True)

        sql = "SELECT * FROM demo_table"

        cursor.execute(sql)

        for row in cursor:
            print(row)


select_messages()


