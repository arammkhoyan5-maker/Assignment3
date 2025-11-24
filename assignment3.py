import os
import json
from pathlib import Path

class StudentManager:
    students = {}

    def add_student(self, name):
        if name in self.students:
            print(f"Student {name} already exists.")
        else:
            self.students[name] = []
            print(f"Student {name} has been added.")

    def add_grade(self, name, grade):
        if name in self.students:
            if 0 <= grade <= 100:
                self.students[name].append(grade)
                print(f"The grade {grade} has been added to {name}'s list")
            else:
                print("The imported number is invalid (0-100).")
        else:
            print(f"The student {name} has not been yet added.")

    def average(self, name):
        if name in self.students and self.students[name]:
            grades_count = len(self.students[name])
            students_average = sum(self.students[name]) / grades_count
            print(f"The average of {name} is {students_average}")
        else:
            print(f"Student {name} has no grades.")

    def show_all(self):
        if not self.students:
            print("No students to show.")
        else:
            for name, grades in self.students.items():
                print(f"{name}: {grades}")

    def save_to_file(self, filename):
        if not filename.endswith('.json'):
            filename = os.path.splitext(filename)[0] + '.json'

        with open(filename, "w") as file:
            json.dump(self.students, file)
            print(f"The file has been successfully saved with .json format")

    def load_from_file(self, filename):
        if Path(filename).exists():
            if os.path.splitext(filename)[1] != ".json":
                print("Please choose a file with .json format.")
                return
            with open(filename, "r") as file:
                loaded_students = json.load(file)
                self.students.update(loaded_students)
                print("The file has been successfully loaded.")
        else:
            print("The file does not exist.")

    def top3(self):
        students_average = {}
        for name, grades in self.students.items():
            if grades:
                average = sum(grades) / len(grades)
                students_average[name] = average
        sorted_students = sorted(students_average.items(), key=lambda x: x[1], reverse=True)
        print("Top 3 students by average grade:")
        for i, (name, average) in enumerate(sorted_students[:3]):
            print(f"{i + 1}. {name}: {average}")

    def delete_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"Student {name} and their grades have been deleted.")
        else:
            print(f"Student {name} not found.")

    def menu(self):
        print("1. Add student\n"
              "2. Add grade\n"
              "3. Show average for student\n"
              "4. Show all students\n"
              "5. Save to file\n"
              "6. Load from file\n"
              "7. Delete student\n"
              "8. Top 3 students\n"
              "9. Exit")

        while True:
            choice = int(input("\nChoose an option: "))
            if choice == 1:
                name = input("Enter name :")
                self.add_student(name)
            elif choice == 2:
                name = input("Enter name :")
                grade = int(input("Enter grade :"))
                self.add_grade(name, grade)
            elif choice == 3:
                name = input("Enter name :")
                self.average(name)
            elif choice == 4:
                self.show_all()
            elif choice == 5:
                filename = input("Enter the file name :")
                self.save_to_file(filename)
            elif choice == 6:
                filename = input("Enter the file name :")
                self.load_from_file(filename)
            elif choice == 7:
                name = input("Enter name of student to delete :")
                self.delete_student(name)
            elif choice == 8:
                self.top3()
            elif choice == 9:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
