import sqlite3

def initialize_db():
    """Sets up the connection and the table."""
    conn = sqlite3.connect("admissions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks INTEGER,
            entrance_score INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    return conn

def save_student(conn, name, marks, entrance, status):
    """Saves a single student record."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, marks, entrance_score, status) 
        VALUES (?, ?, ?, ?)
    ''', (name, marks, entrance, status))
    conn.commit()

def show_all_students(conn):
    """Fetches and prints everything in the students table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall() # This grabs all the data
    
    print("\n--- ALL REGISTERED STUDENTS ---")
    for row in rows:
        print(row)


def delete_all_data(conn):
    """Deletes the entire students table and all records."""
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS students")
    conn.commit()
    print("Database wiped successfully.")

def delete_student_by_id(conn, student_id):
    """Deletes a specific student using their unique ID."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Student with ID {student_id} has been removed.")

    
if __name__ == "__main__":
    # This part only runs if you run database.py directly
    connection = sqlite3.connect("admissions.db")
    show_all_students(connection)
    connection.close()