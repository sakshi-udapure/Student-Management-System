import sqlite3

# Database connect
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Table create
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
''')

conn.commit()

# Add student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    print("Student Added Successfully!")

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\nStudent Records:")
    for row in records:
        print(row)

# Delete student
def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (student_id,)
    )

    conn.commit()

    print("Student Deleted!")

# Menu
while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        delete_student()

    elif choice == '4':
        break

    else:
        print("Invalid Choice")