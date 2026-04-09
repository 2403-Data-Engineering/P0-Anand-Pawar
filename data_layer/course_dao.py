from data_layer.db_connection_manager import get_connection


def insert_course(class_name, subject_code, professor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO course (class_name, subject_code, professor_id, active)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (class_name, subject_code, professor_id, True))
        conn.commit()

        return cursor.lastrowid
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_all_courses():
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
            c.active,
            CONCAT(p.first_name, ' ', p.last_name) AS professor_name
        FROM course c
        LEFT JOIN professor p
            ON c.professor_id = p.professor_id
        WHERE c.active = 1
        ORDER BY c.course_id
        """
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def fetch_course_by_id(course_id):
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
            c.active,
            CONCAT(p.first_name, ' ', p.last_name) AS professor_name
        FROM course c
        LEFT JOIN professor p
            ON c.professor_id = p.professor_id
        WHERE c.course_id = %s
          AND c.active = 1
        """
        cursor.execute(sql, (course_id,))
        return cursor.fetchone()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_course(course_id, class_name, subject_code, professor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE course
        SET class_name = %s,
            subject_code = %s,
            professor_id = %s
        WHERE course_id = %s
          AND active = 1
        """
        cursor.execute(sql, (class_name, subject_code, professor_id, course_id))
        conn.commit()

        return cursor.rowcount
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def course_has_enrollments(course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT COUNT(*) AS enrollment_count
        FROM enrollment
        WHERE course_id = %s
        """
        cursor.execute(sql, (course_id,))
        result = cursor.fetchone()

        return result["enrollment_count"] > 0
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def delete_course(course_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        UPDATE course
        SET active = 0
        WHERE course_id = %s
          AND active = 1
        """
        cursor.execute(sql, (course_id,))
        conn.commit()

        return cursor.rowcount
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def fetch_courses_by_professor(professor_id):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT
            course_id,
            class_name,
            subject_code,
            professor_id,
            active
        FROM course
        WHERE professor_id = %s
          AND active = 1
        ORDER BY course_id
        """
        cursor.execute(sql, (professor_id,))
        return cursor.fetchall()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()