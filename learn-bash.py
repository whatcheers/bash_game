import random
from colorama import Fore, Style, init
import time
import os
from level1_questions import level1_questions
from level2_questions import level2_questions
from level3_questions import level3_questions

# Initialize colorama
init(autoreset=True)

# Check if we're on Windows
is_windows = os.name == 'nt'

if is_windows:
    import winsound

def beep(frequency, duration):
    """
    Play a beep sound.
    On Windows, use winsound. On other systems, print a "beep" message.
    """
    if is_windows:
        winsound.Beep(frequency, duration)
    else:
        print(f"{Fore.YELLOW}BEEP! (Frequency: {frequency}, Duration: {duration}){Style.RESET_ALL}")
        time.sleep(duration / 1000)  # Sleep for the duration in seconds

def correct_sound():
    """Play a sequence of beeps for a correct answer."""
    beep(440, 100)  # A4
    time.sleep(0.05)
    beep(554, 100)  # C#5
    time.sleep(0.05)
    beep(659, 200)  # E5

def incorrect_sound():
    """Play a sequence of beeps for an incorrect answer."""
    beep(392, 200)  # G4
    time.sleep(0.05)
    beep(349, 400)  # F4

def level_complete_sound():
    """Play a triumphant sequence of beeps for completing a level."""
    beep(523, 100)  # C5
    time.sleep(0.05)
    beep(659, 100)  # E5
    time.sleep(0.05)
    beep(784, 100)  # G5
    time.sleep(0.05)
    beep(1046, 400)  # C6

def calculate_points(start_time, is_correct):
    if not is_correct:
        return -10
    elapsed_time = min(time.time() - start_time, 3)
    return max(int(10 + (3 - elapsed_time) * 5), 10)  # Ensure minimum 10 points for correct answers

def display_question(question):
    print(f"\n{Fore.CYAN}{question['question']}{Style.RESET_ALL}")
    options = question['options'].copy()
    random.shuffle(options)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return options

def get_user_answer():
    return input(f"{Fore.YELLOW}Your answer (number): {Style.RESET_ALL}")

def validate_answer(user_answer, correct_answer, options):
    try:
        return options[int(user_answer) - 1] == correct_answer
    except (ValueError, IndexError):
        return False

def main():
    player_points = 0
    current_level = 1
    levels = {
        1: {"questions": level1_questions, "description": "Level 1: Basic Commands"},
        2: {"questions": level2_questions, "description": "Level 2: Intermediate Commands"},
        3: {"questions": level3_questions, "description": "Level 3: Advanced Commands"}
    }

    print(f"{Fore.GREEN}Welcome to Bash Mastery Quiz! Test your knowledge of Bash commands.{Style.RESET_ALL}")
    correct_sound()

    while current_level in levels:
        print(f"\n{Fore.MAGENTA}{levels[current_level]['description']}{Style.RESET_ALL}")
        
        for question in levels[current_level]['questions']:
            options = display_question(question)
            start_time = time.time()
            user_answer = get_user_answer()
            
            if validate_answer(user_answer, question['answer'], options):
                points = calculate_points(start_time, True)
                player_points += points
                print(f"{Fore.GREEN}Correct! You earned {points} points.{Style.RESET_ALL}")
                correct_sound()
                print(f"{Fore.BLUE}Explanation: {question['explanation']}{Style.RESET_ALL}")
            else:
                points = calculate_points(start_time, False)
                player_points += points
                print(f"{Fore.RED}Incorrect. You lost {abs(points)} points.{Style.RESET_ALL}")
                incorrect_sound()
                print(f"{Fore.BLUE}Explanation: {question['explanation']}{Style.RESET_ALL}")
            
            print(f"Current score: {player_points}")

        print(f"\n{Fore.YELLOW}Level {current_level} Complete! You have {player_points} points.{Style.RESET_ALL}")
        level_complete_sound()
        
        if player_points >= current_level * 70:
            print(f"{Fore.GREEN}Congratulations! You've advanced to Level {current_level + 1}.{Style.RESET_ALL}\n")
            current_level += 1
        else:
            print(f"{Fore.RED}You need more points to advance. Try this level again.{Style.RESET_ALL}")
            player_points = (current_level - 1) * 70

    print(f"\n{Fore.GREEN}Congratulations! You've completed all levels of Bash Mastery Quiz!{Style.RESET_ALL}")
    level_complete_sound()

if __name__ == "__main__":
    main()