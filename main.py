# -------------------------------
# Student Management System
# -------------------------------

FILE_NAME = "students.txt"


# ---- Add Student ----
def add_student():
    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("ID cannot be empty!")
        return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    course = input("Enter Student Course: ").strip()

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("✅ Student added successfully!")


# ---- View Students ----
def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
                return

            print("\n--- Student Records ---")
            for line in data:
                student_id, name, age, course = line.strip().split(",")
                print(f"ID: {student_id} | Name: {name} | Age: {age} | Course: {course}")

    except FileNotFoundError:
        print("No student records found.")


# ---- Search Student ----
def search_student():
    search_id = input("Enter Student ID to search: ").strip()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                student_id, name, age, course = line.strip().split(",")

                if student_id == search_id:
                    print("\n🎯 Student Found:")
                    print(f"ID: {student_id} | Name: {name} | Age: {age} | Course: {course}")
                    found = True
                    break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# ---- Update Student ----
def update_student():
    search_id = input("Enter Student ID to update: ").strip()
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                student_id, name, age, course = line.strip().split(",")

                if student_id == search_id:
                    print("Enter new details:")
                    name = input("New Name: ").strip()
                    age = input("New Age: ").strip()
                    course = input("New Course: ").strip()
                    updated = True

                file.write(f"{student_id},{name},{age},{course}\n")

        if updated:
            print("✅ Student updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# ---- Delete Student ----
def delete_student():
    search_id = input("Enter Student ID to delete: ").strip()
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in lines:
                student_id, name, age, course = line.strip().split(",")

                if student_id != search_id:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("🗑 Student deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


# ---- Main Menu ----
while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("👋 Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")