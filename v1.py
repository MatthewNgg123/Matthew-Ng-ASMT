# Dictionary to store student names and their scores
gradebook = {}

while True:
    # Display menu options
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search for Student")
    print("4. Save and Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("Student name: ")

        while True:
            score1 = input("Score 1 (0-100): ")
            if score1.isdigit():
                s1 = int(score1)
                if 0 <= s1 <= 100:
                    break
                else:
                    print("Score must be between 0 and 100.")
            else:
                print("Invalid input. Please enter a whole number.")

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

        avg = (s1 + s2 + s3) / 3
        gradebook[name] = [s1, s2, s3]

        print(f"\nStudent: {name}")
        print(f"Scores: {s1}, {s2}, {s3}")
        print(f"Average: {avg:.2f}")
        print("Student added.\n")

    elif choice == "2":
        if gradebook:
            for name, scores in gradebook.items():
                avg = sum(scores) / len(scores)
                print(f"{name} - Scores: {scores} - Average: {avg:.2f}")
        else:
            print("No students in the gradebook yet.")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in gradebook:
            scores = gradebook[name]
            avg = sum(scores) / len(scores)
            print(f"{name} - Scores: {scores} - Average: {avg:.2f}")
        else:
            print("Student not found.")

    elif choice == "4":
        print("Saved and exiting.")
        break

    else:
        print("Invalid option. Please choose 1-4.")
