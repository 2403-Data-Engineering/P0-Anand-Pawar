from data_layer.db_connection_manager import get_connection


def insert_student(first_name, last_name, email, major, year_level):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO student (first_name, last_name, email, major, year_level, active)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (first_name, last_name, email, major, year_level, True))
        conn.commit()

        return cursor.lastrowid
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_all_students():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT student_id, first_name, last_name, email, major, year_level, active
        FROM student
        WHERE active = 1
        ORDER BY student_id
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_student_by_id(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT student_id, first_name, last_name, email, major, year_level, active
        FROM student
        WHERE student_id = %s AND active = 1
        """
        cursor.execute(sql, (student_id,))
        return cursor.fetchone()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_student(student_id, first_name, last_name, email, major, year_level):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE student
        SET first_name = %s,
            last_name = %s,
            email = %s,
            major = %s,
            year_level = %s
        WHERE student_id = %s
          AND active = 1
        """
        cursor.execute(sql, (first_name, last_name, email, major, year_level, student_id))
        conn.commit()

        return cursor.rowcount
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def student_has_enrollments(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT COUNT(*) AS enrollment_count
        FROM enrollment
        WHERE student_id = %s
        """
        cursor.execute(sql, (student_id,))
        result = cursor.fetchone()

        return result["enrollment_count"] > 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def delete_student(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE student
        SET active = 0
        WHERE student_id = %s
          AND active = 1
        """
        cursor.execute(sql, (student_id,))
        conn.commit()

        return cursor.rowcount
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()