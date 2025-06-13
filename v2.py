# This is the version 2 of my Student Gradebook Program

# A dictionary to store student names as keys and a list of their three scores as values
gradebook = {}

# This function prompts the user to enter a valid score between 0 and 100
def get_score(prompt):
    while True:
        value = input(prompt).strip()  # Removes whitespaces
        if value == "":
            print("Nothing was entered. Please enter a score.")
            continue  # Ask again if nothing was typed
        try:
            number = float(value)  # Converting input to a float
            if 0 <= number <= 100:
                return number  # Valid score entered
            else:
                print("Score must be between 0 and 100.")  # Score out of range
        except:
            print("Please enter a valid number.")  # Input was not numeric

# This function allows the user to add a new student and their three scores
def add_student():
    name = input("Enter student name: ").strip()  # Gets the student's name and removes any whitespaces
    if not name:
        print("Student name cannot be empty.")
        return  # Exit if no name was entered

    if name in gradebook:
        # Warn user that student already exists
        answer = input("This student already exists. Overwrite? (yes/no): ").strip().lower() # Removes whitespaces and converts to lowercase
        if answer != "yes":
            print("Student not added.")
            return  # Exit without overwriting if user says no

    # Prompt user for three valid scores
    s1 = get_score("Enter score 1: ")
    s2 = get_score("Enter score 2: ")
    s3 = get_score("Enter score 3: ")

    # Store the scores in the gradebook under the student's name
    gradebook[name] = [s1, s2, s3]

    # Calculate and display the average score
    average = round((s1 + s2 + s3) / 3, 2)
    print(f"Student '{name}' added with average score: {average}")

# This function displays all students in the gradebook along with their scores and averages
def show_all_students():
    if not gradebook:
        print("No students in the gradebook.")
        return  # Exit if there are no students

    # Loop through each student and display their data
    for name, scores in gradebook.items():
        average = round(sum(scores) / 3, 2)  # Calculate average score
        print(f"\nStudent: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {average}")

# This function searches for a student by name and displays their scores
def search_student():
    name = input("Enter student name to search: ").strip() # Removes whitespaces
    if name in gradebook:
        scores = gradebook[name]
        average = round(sum(scores) / 3, 2)
        print(f"\nStudent: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {average}")
    else:
        print("Student not found.")  # Inform user if student does not exist

# This function saves the current gradebook to a text file and exits the program
def save_and_exit():
    if not gradebook:
        print("No data to save.")  # Avoid saving empty data
        return True  # Still return True to allow exiting

    try:
        # Open the file in append mode so previous data is not overwritten
        with open("Matthew Ng-ASMT/v2report.txt", "a") as file:
            file.write("====== Gradebook Report ======\n")
            for name, scores in gradebook.items():
                average = round(sum(scores) / 3, 2)
                file.write(f"Name: {name}\nScores: {scores}\nAverage: {average}\n")
            file.write("-" * 30 + "\n")  # Separator line
        print("Report saved successfully.")
    except:
        print("An error occurred while saving the file.")  # Handle unexpected file errors

    return True  # Signal to main loop to exit

# Main program loop starts here

while True:
    # Display main menu options
    print("\nGradebook Menu:")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Save and Exit")

    # Get user menu choice
    choice = input("Enter your choice (1-4): ")

    # Call the appropriate function based on user's choice
    if choice == "1":
        add_student()
    elif choice == "2":
        show_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        if save_and_exit():  # Save and exit only if function returns True
            break  # Break the loop and end the program
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
