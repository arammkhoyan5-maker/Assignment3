import json
from pathlib import Path

class StudentManager:
    students = {}

    def add_student ( students , name ):
        if name in students:
            print(f"Student {name} already exists.")
        else:
            students[name] = []
            print(f"Student {name} has been added.")

    def add_grade ( students , name , grade ):
        if name in students:
            if 0 <= grade <= 100:
                students[name].append(grade)
                print(f"The grade {grade} has been added to {name}'s list")
            else:
                print("The imported number is invalid (0-100).")
        else:
            print(f"The student {name} has not been yet added.")

    def average ( students , name ):

        grades_count = len(students[name])
        students_average = sum(students[name])/ grades_count
        print(f"The average of {name} is {students_average}")

    def show_all(self):
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

    def top3(students):
        # Create a dictionary to store averages
        students_average = {}

        for name, grades in students.items():
            if grades:
                average = sum(grades) / len(grades)
                students_average[name] = average

        # Sort the students by average in descending order using sorted
        sorted_students = sorted(students_average.items(), key=lambda x: x[1], reverse=True)

        # Display the top 3 students
        print("Top 3 students by average grade:")
        for i, (name, average) in enumerate(sorted_students[:3]):
            print(f"{i + 1}. {name}: {average}")

    print("1. Add student\n"
          "2. Add grade\n"
          "3. Show average for student\n"
          "4. Show all students\n"
          "5. Save to file\n"
          "6. Load from file\n"
          "7. Top 3 students\n"
          "8. Exit\n")

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
            top3(students)

        elif choice == 8:
            exit()
