from data_layer.db_connection_manager import get_connection


def enrollment_exists(student_id, course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT enrollment_id
        FROM enrollment
        WHERE student_id = %s
          AND course_id = %s
        """
        cursor.execute(sql, (student_id, course_id))
        return cursor.fetchone() is not None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def insert_enrollment(student_id, course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO enrollment (student_id, course_id)
        VALUES (%s, %s)
        """
        cursor.execute(sql, (student_id, course_id))
        conn.commit()

        return cursor.lastrowid
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def delete_enrollment(student_id, course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE FROM enrollment
        WHERE student_id = %s
          AND course_id = %s
        """
        cursor.execute(sql, (student_id, course_id))
        conn.commit()

        return cursor.rowcount
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_students_by_course(course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT
            s.student_id,
            s.first_name,
            s.last_name,
            s.email,
            s.major,
            s.year_level
        FROM enrollment e
        INNER JOIN student s
            ON e.student_id = s.student_id
        INNER JOIN course c
            ON e.course_id = c.course_id
        WHERE e.course_id = %s
          AND s.active = 1
          AND c.active = 1
        ORDER BY s.student_id
        """
        cursor.execute(sql, (course_id,))
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_courses_by_student(student_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT
            c.course_id,
            c.class_name,
            c.subject_code,
            c.professor_id,
            CONCAT(p.first_name, ' ', p.last_name) AS professor_name
        FROM enrollment e
        INNER JOIN course c
            ON e.course_id = c.course_id
        INNER JOIN student s
            ON e.student_id = s.student_id
        LEFT JOIN professor p
            ON c.professor_id = p.professor_id
        WHERE e.student_id = %s
          AND c.active = 1
          AND s.active = 1
        ORDER BY c.course_id
        """
        cursor.execute(sql, (student_id,))
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()