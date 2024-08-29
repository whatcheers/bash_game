import random

# Define game scenarios and commands for each level
levels = {
    1: {
        "category": "File Management",
        "description": "Level 1: Learn to manage files and directories.",
        "tasks": [
            {"description": "List all files in the current directory.", "command": "ls"},
            {"description": "Create a directory named 'test'.", "command": "mkdir test"},
            {"description": "Remove the directory named 'test'.", "command": "rmdir test"},
        ],
        "quiz": [
            {"question": "What command lists files in a directory?", "options": ["ls", "cd", "pwd"], "answer": "ls"},
            {"question": "How do you create a new directory?", "options": ["mkdir", "rmdir", "touch"], "answer": "mkdir"},
        ]
    },
    2: {
        "category": "System Information",
        "description": "Level 2: Learn commands to check system information.",
        "tasks": [
            {"description": "Display the system's kernel version.", "command": "uname -r"},
            {"description": "Show disk usage in human-readable format.", "command": "df -h"},
        ],
        "quiz": [
            {"question": "Which command displays the kernel version?", "options": ["uname -r", "ls", "df -h"], "answer": "uname -r"},
            {"question": "How do you check disk usage?", "options": ["free -h", "df -h", "du"], "answer": "df -h"},
        ]
    },
    # Add more levels as needed
}

# Initialize player points and current level
player_points = 0
current_level = 1

def display_scenario(level):
    """Display the level description and tasks."""
    print("\n" + levels[level]["description"])
    tasks = levels[level]["tasks"]
    return tasks

def get_user_command(task):
    """Prompt user for input based on task."""
    print("\nTask: " + task["description"])
    return input("> ")

def validate_command(user_command, correct_command):
    """Check if the user input matches the correct command."""
    return user_command.strip() == correct_command.strip()

def conduct_quiz(level):
    """Conduct a quiz based on the completed level."""
    quiz_questions = levels[level]["quiz"]
    quiz_score = 0
    print("\nQuiz Time! Answer the following questions:")

    for question in quiz_questions:
        print("\n" + question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        answer = input("Your answer (number): ")

        # Validate answer
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            quiz_score += 1
        else:
            print(f"Incorrect. The correct answer is '{question['answer']}'.")
    
    return quiz_score

def main():
    global player_points, current_level
    
    print("Welcome to Bash Mastery Adventure! Learn Bash commands to advance through different levels.")
    
    while current_level in levels:
        # Display the current level and its tasks
        tasks = display_scenario(current_level)
        for task in tasks:
            while True:
                user_command = get_user_command(task)
                if validate_command(user_command, task["command"]):
                    print("Correct!")
                    player_points += 10  # Add points for correct task
                    break
                else:
                    print("Incorrect. Try again or type 'hint' for a clue.")
                    if user_command.lower() == 'hint':
                        print(f"Hint: The command starts with '{task['command'].split()[0]}'.")

        # Conduct quiz after completing the tasks of the current level
        quiz_score = conduct_quiz(current_level)
        player_points += quiz_score * 10  # Add points for correct quiz answers

        # Check if player can advance to the next level
        print(f"\nLevel {current_level} Complete! You have {player_points} points.")
        if player_points >= current_level * 20:  # Points required to advance increase with level
            print(f"Congratulations! You've advanced to Level {current_level + 1}.\n")
            current_level += 1
        else:
            print("You need more points to advance to the next level. Try the quiz again.")
    
    print("\nCongratulations! You've completed all levels of Bash Mastery Adventure and learned essential Bash commands!")

if __name__ == "__main__":
    main()
