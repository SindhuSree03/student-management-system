# ---- Function 1 ----
def add_student():
    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("ID cannot be empty!")
        return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    course = input("Enter Student Course: ").strip()

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("Student added successfully!")


# ---- Function 2 ----
def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()

            if not data:
                print("No student records found.")
            else:
                print("\n--- Student Records ---")
                print("-" * 50)
                print(f"{'ID':<10}{'Name':<15}{'Age':<10}{'Course':<15}")
                print("-" * 50)

                for line in data:
                    student_id, name, age, course = line.strip().split(",")
                    print(f"{student_id:<10}{name:<15}{age:<10}{course:<15}")

                print("-" * 50)

    except FileNotFoundError:
        print("No student records found.")


# ---- Function 3 ----
def search_student():
    search_id = input("Enter Student ID to search: ")
    found = False

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, age, course = line.strip().split(",")

                if student_id == search_id:
                    print("\nStudent Found:")
                    print(f"ID: {student_id} | Name: {name} | Age: {age} | Course: {course}")
                    found = True
                    break

        if not found:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")

def update_student():
    update_id = input("Enter Student ID to update: ")
    updated = False
    lines = []

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                student_id, name, age, course = line.strip().split(",")

                if student_id == update_id:
                    print("Enter new details:")
                    name = input("New Name: ")
                    age = input("New Age: ")
                    course = input("New Course: ")
                    updated = True

                file.write(f"{student_id},{name},{age},{course}\n")

        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")


def delete_student():
    delete_id = input("Enter Student ID to delete: ")
    deleted = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                student_id, name, age, course = line.strip().split(",")

                if student_id != delete_id:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except FileNotFoundError:
        print("No student records found.")

# ---- Main Program ----
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. update student")
    print("5. delete student")
    print("6. exit")

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
        break
    else:
        print("Invalid choice")