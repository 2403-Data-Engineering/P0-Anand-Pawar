from data_layer.db_connection_manager import get_connection

def insert_professor(first, last, dept, email):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO professor (first_name, last_name, department, email, active)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, (first, last, dept, email, True))
    conn.commit()
    ret = cursor.lastrowid
    cursor.close()
    conn.close()
    return ret

def fetch_all_professors():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT * 
    FROM professor
    WHERE active = 1
    ORDER BY professor_id
    """

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

def fetch_professor_by_id(professor_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT * 
    FROM professor
    WHERE professor_id = %s AND active = 1
    """

    cursor.execute(sql,(professor_id))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result


def update_professor(prof_id, first, last, dept, email):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE professor
    SET first_name=%s, last_name=%s, department=%s, email=%s
    WHERE professor_id=%s AND active = 1
    """

    cursor.execute(sql, (first, last, dept, email, prof_id))
    conn.commit()
    row = cursor.rowcount
    cursor.close()
    conn.close()
    return row

def professor_has_courses(professor_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT COUNT(*) AS course_count
    FROM course
    WHERE professor_id = %s AND active = 1
    """
    cursor.execute(sql, (professor_id))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result["course_count"] > 0

def delete_professor(prof_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        UPDATE professor
        SET active = 0
        WHERE professor_id = %s
          AND active = 1
        """
    
    cursor.execute(sql, (prof_id,))
    conn.commit()
    done = cursor.rowcount

    cursor.close()
    conn.close()
    return done