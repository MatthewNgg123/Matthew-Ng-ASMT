# This is the version 3 of my Student Gradebook Program

from easygui import *

# Constants & Initial Setup

# Path where the final gradebook report will be saved as a text file.
FILE_PATH = "Matthew Ng-ASMT/v3report.txt"

# Title used in all GUI windows for consistency
TITLE = "📚 Student Gradebook"

# Menu options the user can select from on the main screen
MENU_ADD = "+ Add Student"
MENU_SHOW = "📄 Show All Students"
MENU_SEARCH = "🔍 Search Student"
MENU_SAVE_EXIT = "💾 Save and Exit"

# These choices will appear as buttons in the main menu
MENU_OPTIONS = [MENU_ADD, MENU_SHOW, MENU_SEARCH, MENU_SAVE_EXIT]

# A visual separator used in the saved text report to divide students
SEPARATOR = "-" * 30

# Constants that define score range and how many scores per student
MIN_SCORE = 0
MAX_SCORE = 100
NUM_SCORES = 3

# Dictionary used to store all student records in memory
# Format: { "Alice": [score1, score2, score3], "Bob": [...] }
gradebook = {}


# Input Validation Functions

def get_valid_name():
    """
    Prompt user for a student name.
    Only allows alphabet letters (A-Z or a-z), no spaces or symbols.
    """
    while True:
        name = enterbox("Enter student name (letters only):", title=TITLE)

        if name is None:
            cancel = buttonbox("Cancel adding student?", choices=["Yes", "No"], title=TITLE)
            if cancel == "Yes":
                return None
            else:
                continue

        name = name.strip()

        if name == "":
            msgbox("⚠️ Name cannot be empty.", title=TITLE)
            continue

        if name.isalpha():
            return name
        else:
            msgbox("❌ Name must only contain letters (A-Z). No spaces or symbols.", title=TITLE)

def get_valid_score(message):
    """
    Prompts the user for a single score, validates it is a number within 0-100,
    and handles cancel operations gracefully.
    Returns:
        float: A valid score entered by the user, or None if canceled.
    """
    while True:
        score = enterbox(message, title=TITLE)

        if score is None:
            # Confirm cancelation
            cancel = buttonbox("Cancel adding this student?", choices=["Yes", "No"], title=TITLE)
            if cancel == "Yes":
                return None
            else:
                continue

        try:
            score_float = round(float(score), 2)

            if MIN_SCORE <= score_float <= MAX_SCORE:
                return score_float
            else:
                msgbox(f"⚠️ Score must be between {MIN_SCORE} and {MAX_SCORE}.", title=TITLE)

        except ValueError:
            msgbox("❌ Invalid input. Please enter a number.", title=TITLE)


# Display Functions

def show_all_students():
    """
    Show all students currently in the gradebook.
    Lists each student's name, their scores, and calculated average.
    If no students exist, shows a message.
    """
    if not gradebook:
        msgbox("📭 No students added yet.", title=TITLE)
        return

    report = ""
    for name, scores in gradebook.items():
        avg = round(sum(scores) / NUM_SCORES, 2)
        report += f"👤 {name}\n📝 Scores: {scores}\n📊 Average: {avg}\n\n"

    # Display all student info in a scrollable textbox
    textbox("📋 All Students", text=report, title=TITLE)

def search_student():
    """
    Ask user for a name and search for that student in the gradebook.
    If found, display the student's scores and average.
    If not found, show a warning.
    """
    search_name = enterbox("Enter student name to search:", title=TITLE)

    if not search_name:
        return

    if search_name in gradebook:
        scores = gradebook[search_name]
        avg = round(sum(scores) / NUM_SCORES, 2)
        msgbox(f"👤 {search_name}\n📝 Scores: {scores}\n📊 Average: {avg}", title=TITLE)
    else:
        msgbox("⚠️ Student not found.", title=TITLE)

# 💾 File Handling Function

def save_gradebook():
    """
    Write the current gradebook to a text file in a readable report format.
    Returns:
        bool: True if saved successfully, False if any error occurs.
    """
    try:
        with open(FILE_PATH, "a") as file:
            file.write("=== Student Gradebook Report ===\n\n")
            for name, scores in gradebook.items():
                avg = round(sum(scores) / NUM_SCORES, 2)
                file.write(f"Name: {name}\n")
                file.write(f"Scores: {scores[0]}, {scores[1]}, {scores[2]}\n")
                file.write(f"Average: {avg}\n")
                file.write(SEPARATOR + "\n")
        return True
    except:
        msgbox("❌ Error saving file.", title=TITLE)
        return False

# 🚀 Main Menu and Control Flow

def main():
    """
    Main loop for user interaction.
    Continuously presents menu options and handles the logic
    for each selected task (Add, Show, Search, Save/Exit).
    """
    while True:
        choice = buttonbox("Choose an option:", title=TITLE, choices=MENU_OPTIONS)

        if choice == MENU_ADD:
            # Get student name and check if already exists
            name = get_valid_name()
            if name is None:
                continue

            if name in gradebook:
                overwrite = buttonbox(f"⚠️ Student '{name}' already exists. Overwrite?",
                    choices=["Yes", "No"], title=TITLE)
                if overwrite != "Yes":
                    continue

            # Collect exactly 3 scores for the new student
            s1 = get_valid_score("Enter Score 1 (0-100):")
            if s1 is None: continue
            s2 = get_valid_score("Enter Score 2 (0-100):")
            if s2 is None: continue
            s3 = get_valid_score("Enter Score 3 (0-100):")
            if s3 is None: continue

            # Save student to gradebook
            gradebook[name] = [s1, s2, s3]
            avg = round((s1 + s2 + s3) / NUM_SCORES, 2)

            # Confirmation message
            msgbox(f"👤 Student: {name}\n📝 Scores: {s1}, {s2}, {s3}\n📊 Average: {avg}\n✅ Student added.", title=TITLE)

        elif choice == MENU_SHOW:
            # View all students and their grades
            show_all_students()

        elif choice == MENU_SEARCH:
            # Search for one specific student
            search_student()

        elif choice == MENU_SAVE_EXIT:
            # Exit program after optionally saving the data
            if not gradebook:
                msgbox("⚠️ No data to save.", title=TITLE)
                break

            if save_gradebook():
                msgbox("✅ Report saved. Exiting program.", title=TITLE)
            break

# Program starts here

if __name__ == "__main__":
    # Run the main application loop
    main()
