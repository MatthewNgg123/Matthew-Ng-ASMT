'''
This is the first version of my Student Gradebook Manager.
'''

# Dictionary to store student names as keys and a list of their scores as values
gradebook = {}

# Start an infinite loop to display the menu and take user input repeatedly
while True:
    # Display menu options for the user
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search for Student")
    print("4. Save and Exit")

    # Prompt user to choose an option
    choice = input("Choose (1-4): ")

    # Option 1: Add a student and their scores
    if choice == "1":
        name = input("Student name: ")  # Get the student's name

        # Input validation loop for Score 1
        while True:
            score1 = input("Score 1 (0-100): ")
            if score1.isdigit():  # Check if input is a digit
                s1 = int(score1)
                if 0 <= s1 <= 100:  # Ensure the score is within valid range
                    break
                else:
                    print("Score must be between 0 and 100.")
            else:
                print("Invalid input. Please enter a whole number.")

        # Input validation loop for Score 2
        while True:
            score2 = input("Score 2 (0-100): ")
            if score2.isdigit():
                s2 = int(score2)
                if 0 <= s2 <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")
            else:
                print("Invalid input. Please enter a whole number.")

        # Input validation loop for Score 3
        while True:
            score3 = input("Score 3 (0-100): ")
            if score3.isdigit():
                s3 = int(score3)
                if 0 <= s3 <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")
            else:
                print("Invalid input. Please enter a whole number.")

        # Calculate average score
        avg = (s1 + s2 + s3) / 3

        # Store the scores in the gradebook dictionary
        gradebook[name] = [s1, s2, s3]

        # Display confirmation and summary
        print(f"\nStudent: {name}")
        print(f"Scores: {s1}, {s2}, {s3}")
        print(f"Average: {avg:.2f}")
        print("Student added.\n")

    # Option 2: Show all students and their scores
    elif choice == "2":
        if gradebook:  # Check if gradebook is not empty
            for name, scores in gradebook.items():  # Loop through each student
                avg = sum(scores) / len(scores)  # Calculate average score
                print(f"{name} - Scores: {scores} - Average: {avg:.2f}")
        else:
            print("No students in the gradebook yet.")

    # Option 3: Search for a specific student
    elif choice == "3":
        name = input("Enter student name: ")  # Get student name to search
        if name in gradebook:  # Check if student exists
            scores = gradebook[name]
            avg = sum(scores) / len(scores)
            print(f"{name} - Scores: {scores} - Average: {avg:.2f}")
        else:
            print("Student not found.")

    # Option 4: Exit the program
    elif choice == "4":
        print("Saved and exiting.")
        break  # Exit the while loop and end the program

    # Handle invalid menu input
    else:
        print("Invalid option. Please choose 1-4.")
