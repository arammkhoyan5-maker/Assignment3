import json
from pathlib import Path


students = {}

def add_student ( students , name ):
    if name in students:
        print(f"Student {name} already exists.")
    else:
        students[name] = []
        print(f"Student {name} has been added.")

def add_grade ( students , name , grade ):
    if name in students:
        students[name].append(grade)
        print(f"The grade {grade} has been added to {name}'s list")
    else:
        print(f"The student {name} has not been yet added.")

def average ( students , name ):

    grades_count = len(students[name])
    students_average = sum(students[name])/ grades_count
    print(f"The average of {name} is {students_average}")

def show_all ():
    for name in students.keys():
        print(f"{name}: {students[name]}")


def save_to_file(students, filename):

    with open(filename,"w") as file:
        json.dump(students,file)
        print("The file has been successfully saved")

def load_from_file ( filename ) :
    if Path(filename).exists():
        with open(filename,"r") as file:
            loaded_students = json.load(file)
            students.update(loaded_students)
            print("The file has been successfully loaded")
    else:
        print("The file does not exist.")


print("1. Add student\n"
      "2. Add grade\n"
      "3. Show average for student\n"
      "4. Show all students\n"
      "5. Save to file\n"
      "6. Load from file\n"
      "7. Exit\n")

while True:
    choice = int(input("\nChoose an option: "))


    if  choice == 1:
        name = str(input("Enter name :"))
        add_student(students, name)

    elif choice == 2:
        name = str(input("Enter name :"))
        grade = int(input("Enter grade :"))
        add_grade(students, name, grade)

    elif choice == 3:
        name = str(input("Enter name :"))
        average(students, name)

    elif choice == 4:
        show_all()

    elif choice == 5:
        filename = str(input("Enter the file name :"))
        save_to_file(students, filename)

    elif choice == 6:
        filename = str(input("Enter the file name :"))
        load_from_file(filename)

    elif choice == 7:
        exit()
