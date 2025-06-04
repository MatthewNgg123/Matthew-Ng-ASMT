# A dictionary to store student names and their scores
gradebook = {}

# This function asks the user for a valid score (0-100)
def get_score(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Nothing was entered. Please enter a score.")
            continue
        try:
            number = float(value)
            if 0 <= number <= 100:
                return number
            else:
                print("Score must be between 0 and 100.")
        except:
            print("Please enter a valid number.")

# This function adds a new student to the gradebook
def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    if name in gradebook:
        answer = input("This student already exists. Overwrite? (yes/no): ").strip().lower()
        if answer != "yes":
            print("Student not added.")
            return

    # Get three scores from the user
    s1 = get_score("Enter score 1: ")
    s2 = get_score("Enter score 2: ")
    s3 = get_score("Enter score 3: ")

    # Save the scores in the gradebook
    gradebook[name] = [s1, s2, s3]
    average = round((s1 + s2 + s3) / 3, 2)
    print(f"Student '{name}' added with average score: {average}")

# This function shows all students and their scores
def show_all_students():
    if not gradebook:
        print("No students in the gradebook.")
        return

    for name, scores in gradebook.items():
        average = round(sum(scores) / 3, 2)
        print(f"\nStudent: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {average}")

# This function searches for a specific student
def search_student():
    name = input("Enter student name to search: ").strip()
    if name in gradebook:
        scores = gradebook[name]
        average = round(sum(scores) / 3, 2)
        print(f"\nStudent: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {average}")
    else:
        print("Student not found.")

# This function saves the gradebook to a file and exits
def save_and_exit():
    if not gradebook:
        print("No data to save.")
        return True

    try:
        with open("Matthew Ng-ASMT/v2report.txt", "a") as file:
            file.write("====== Gradebook Report ======\n")
            for name, scores in gradebook.items():
                average = round(sum(scores) / 3, 2)
                file.write(f"Name: {name}\nScores: {scores}\nAverage: {average}\n")
            file.write("-" * 30 + "\n")
        print("Report saved successfully.")
    except:
        print("An error occurred while saving the file.")
    return True

# Main program loop
while True:
    print("\nGradebook Menu:")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Save and Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        if save_and_exit():
            break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
