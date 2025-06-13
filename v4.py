# This is the version 4 of my Student Gradebook Program

from easygui import *         # EasyGUI for graphical dialogs
import matplotlib.pyplot as plt  # For plotting graphs
import random                 # For generating random colors in graphs
import os                     # For file operations

# CONSTANTS 
FILE_PATH = "Matthew Ng-ASMT/v4report.txt"  # Path to save the report
TITLE = "📚 Student Gradebook"               # GUI window title
MENU_OPTIONS = [
    "+ Add Student", 
    "📄 Show All Students", 
    "🔍 Search Student", 
    "❌ Remove Student", 
    "📊 Graph Averages", 
    "💾 Save and Exit"
]
SEPARATOR = "-" * 30         # Visual separator for reports
# Constants for score validation
MIN_SCORE = 0                # Minimum score allowed
MAX_SCORE = 100              # Maximum score allowed
NUM_SCORES = 3               # Number of scores per student

# Dictionary to hold all student data
gradebook = {}

# Get a valid numeric score from the user within MIN and MAX range
def get_valid_score(message):
    """
    Prompt the user for a single score between 0 and 100.
    Ensures input is numeric and within valid range.
    """
    while True:
        score = enterbox(message, title=TITLE)
        if score is None:
            return None
        try:
            score_float = float(score)
            if MIN_SCORE <= score_float <= MAX_SCORE:
                return score_float
            else:
                msgbox(f"⚠️ Score must be between {MIN_SCORE} and {MAX_SCORE}.", title=TITLE)
        except ValueError:
            msgbox("❌ Invalid input. Please enter a number (e.g., 75 or 88.5).", title=TITLE)

def get_valid_name():
    """
    Prompt user for a valid name consisting only of alphabetic letters.
    Prevents use of spaces, symbols, or empty names.
    """
    while True:
        name = enterbox("Enter student name (letters only, no spaces or symbols):", title=TITLE)
        if name is None:
            return None
        name = name.strip()
        if name == "":
            msgbox("❌ No name entered. Please enter a valid name.", title=TITLE)
            continue
        if " " in name:
            msgbox("❌ Spaces are not allowed in the name.", title=TITLE)
            continue
        if name.isalpha():
            return name
        else:
            msgbox("❌ Invalid name. Use letters only (A-Z).", title=TITLE)

# 💾 File Handling Functions

def save_gradebook():
    """
    Save the current gradebook to a text file with formatted scores and averages.
    Returns True if successful, False on error.
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
    except Exception as e:
        msgbox(f"❌ Error saving file: {e}", title=TITLE)
        return False

def load_gradebook():
    """
    Load saved student records from the report file into memory if file exists.
    """
    if not os.path.exists(FILE_PATH):
        return
    try:
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("Name:"):
                name = line[5:].strip()
                i += 1
                if i < len(lines) and lines[i].startswith("Scores:"):
                    scores_line = lines[i][7:].strip()
                    scores = [float(s.strip()) for s in scores_line.split(",")]
                    gradebook[name] = scores
                i += 3
            else:
                i += 1
    except Exception as e:
        msgbox(f"⚠️ Failed to load data: {e}", title=TITLE)

# 📋 Core Student Functions

def add_student():
    """
    Add a new student to the gradebook or overwrite an existing one.
    Collects 3 validated test scores from the user.
    """
    name = get_valid_name()
    if not name:
        return

    existing_name = next((n for n in gradebook if n.lower() == name.lower()), None)
    if existing_name:
        overwrite = buttonbox(f"⚠️ Student '{existing_name}' already exists. Overwrite?", choices=["Yes", "No"], title=TITLE)
        if overwrite != "Yes":
            return
        name = existing_name

    s1 = get_valid_score("Enter Score 1 (0-100):")
    if s1 is None: return
    s2 = get_valid_score("Enter Score 2 (0-100):")
    if s2 is None: return
    s3 = get_valid_score("Enter Score 3 (0-100):")
    if s3 is None: return

    gradebook[name] = [s1, s2, s3]
    avg = round((s1 + s2 + s3) / NUM_SCORES, 2)
    msgbox(f"👤 Student: {name}\n📝 Scores: {s1}, {s2}, {s3}\n📊 Average: {avg}\n✅ Student added.", title=TITLE)

def show_all_students():
    """
    Display all students in a scrollable textbox with scores and averages.
    """
    if not gradebook:
        msgbox("📭 No students added yet.", title=TITLE)
        return

    report = ""
    for name, scores in gradebook.items():
        avg = round(sum(scores) / NUM_SCORES, 2)
        report += f"👤 {name}\n📝 Scores: {scores}\n📊 Average: {avg}\n\n"
    textbox("📋 All Students", text=report, title=TITLE)

def search_student():
    """
    Prompt user to search for a student by name and display their scores.
    """
    search_name = enterbox("Enter student name to search:", title=TITLE)
    if not search_name:
        return

    for student in gradebook:
        if student.lower() == search_name.strip().lower():
            scores = gradebook[student]
            avg = round(sum(scores) / NUM_SCORES, 2)
            msgbox(f"👤 {student}\n📝 Scores: {scores}\n📊 Average: {avg}", title=TITLE)
            return

    msgbox("⚠️ Student not found.", title=TITLE)

def remove_student():
    """
    Ask for a student name and remove them from the gradebook if they exist.
    """
    if not gradebook:
        msgbox("📭 No students to remove.", title=TITLE)
        return

    name_input = enterbox("Enter the name of the student to remove:", title=TITLE)
    if not name_input:
        return

    matched_name = next((n for n in gradebook if n.lower() == name_input.strip().lower()), None)

    if not matched_name:
        msgbox(f"⚠️ Student '{name_input}' not found.", title=TITLE)
        return

    confirm = buttonbox(f"Are you sure you want to remove '{matched_name}'?", title=TITLE, choices=["Yes", "No"])
    if confirm == "Yes":
        del gradebook[matched_name]
        msgbox(f"🗑️ Student '{matched_name}' removed.", title=TITLE)
    else:
        msgbox("❌ Removal cancelled.", title=TITLE)

# 📊 Data Visualization

def graph_averages():
    """
    Generate a bar chart of student average scores using matplotlib.
    """
    if not gradebook:
        msgbox("📭 No students to graph.", title=TITLE)
        return

    names = list(gradebook.keys())
    averages = [round(sum(scores) / NUM_SCORES, 2) for scores in gradebook.values()]
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in names]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, averages, color=colors)
    plt.ylabel("Average Score")
    plt.title("📊 Student Average Scores")
    plt.xticks(rotation=45, ha='right')
    plt.ylim(0, 100)

    for bar, avg in zip(bars, averages):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{avg}", ha='center', fontsize=9)

    plt.tight_layout()
    plt.show()

# 🚀 Main Control Flow

def main():
    """
    Main loop for user interaction through GUI menu buttons.
    Handles loading, saving, and calling feature functions.
    """
    load_gradebook()

    while True:
        choice = buttonbox("Choose an option:", title=TITLE, choices=MENU_OPTIONS)
        if choice is None:
            break

        if choice == "+ Add Student":
            add_student()
        elif choice == "📄 Show All Students":
            show_all_students()
        elif choice == "🔍 Search Student":
            search_student()
        elif choice == "❌ Remove Student":
            remove_student()
        elif choice == "📊 Graph Averages":
            graph_averages()
        elif choice == "💾 Save and Exit":
            if not gradebook:
                msgbox("⚠️ No data to save.", title=TITLE)
                break
            if save_gradebook():
                msgbox("✅ Report saved. Exiting program.", title=TITLE)
            break

# ✅ Start the program
main()