Python Final Project - README
Overview
This Python Final Project, created by Jeff Loula, is an interactive program that includes multiple games and quizzes to entertain and educate users. The program features various challenges such as Hangman, Tic-Tac-Toe, a Math Quiz, the OCEAN Personality Test, and quizzes about the Periodic Table, U.S. State Capitals, and Amendments to the U.S. Constitution.

The program allows users to select a game or quiz from a menu, interact with it, and receive feedback on their performance.

Features
1. Hangman
Objective: Guess the hidden word one letter at a time.
How it works:
The program selects a random word from a predefined list.
The user has 6 attempts to guess the word, one letter at a time.
Feedback is provided after each guess (correct, incorrect, or already guessed).
End condition: The game ends when the user either guesses the word correctly or runs out of attempts.
2. Tic-Tac-Toe (Against Computer)
Objective: Win or draw against the computer in a classic 3x3 grid game.
How it works:
The user plays as "X" and the computer as "O".
The user and computer alternate turns, selecting grid positions.
The game checks for a winner after each move or declares a draw if all spots are filled.
End condition: The game ends with a win, loss, or draw.
3. Math Quiz
Objective: Solve 5 random math problems and achieve the highest possible score.
How it works:
Random math problems are generated, including addition, subtraction, multiplication, integer division, and basic algebra.
The user enters answers, and the program evaluates correctness.
End condition: The user receives a score out of 5 and feedback on each question.
4. OCEAN Personality Test
Objective: Complete a personality assessment based on the Big Five personality traits.
How it works:
The user rates 50 statements on a scale of 1 (Strongly Disagree) to 5 (Strongly Agree).
The program calculates scores for Openness, Conscientiousness, Extroversion, Agreeableness, and Neuroticism.
End condition: The results are displayed and saved to a file.
5. Periodic Table Quiz
Objective: Identify elements based on their symbols.
How it works:
The program provides the symbol of an element, and the user must input the corresponding element name.
The quiz consists of 5 questions selected randomly from the periodic table.
End condition: The user receives a score out of 5.
6. U.S. States and Capitals Quiz
Objective: Match states with their capitals or capitals with their states.
How it works:
The program randomly asks the user either:
The capital of a given state.
The state corresponding to a given capital.
The quiz consists of 5 random questions.
End condition: The user receives a score out of 5.
7. Amendments Quiz
Objective: Identify U.S. Constitutional Amendments based on their descriptions.
How it works:
The program provides the description of an amendment, and the user must input the corresponding amendment number.
The quiz consists of 5 random questions.
End condition: The user receives a score out of 5.
How to Run the Program
Ensure Python is installed on your computer (Python 3.6 or later recommended).
Download the program file (final_project.py) and any additional files (e.g., word_list.txt).
Open a terminal or command prompt.
Navigate to the directory containing the program file.
Run the program using the command:
python final_project.py
How to Use
When the program starts, log in by entering your name.
The main menu will display the available games and quizzes.
Select an option by entering the corresponding number (1-8):
1: Hangman
2: Tic-Tac-Toe
3: Math Quiz
4: OCEAN Personality Test
5: Periodic Table Quiz
6: U.S. States and Capitals Quiz
7: Amendments Quiz
8: Exit the program.
Follow the instructions for the selected game or quiz.
At the end of each game or quiz, feedback and scores are provided.
Error Handling
Invalid Inputs: The program includes error handling for invalid inputs (e.g., entering non-numeric values where numbers are required).
Out of Range Choices: Menu choices outside the valid range prompt the user to try again.
File Handling: The program saves results (where applicable) to files, ensuring unique filenames using timestamps.
Program Flow
Login: The user enters their name, which is used throughout the program.
Main Menu: The user selects a game or quiz from the menu.
Game/Quiz Execution: The program runs the selected activity and provides interactive prompts.
Scoring: Feedback and scores are displayed after each activity.
Repeat or Exit: The user can choose another game/quiz or exit the program.
File Structure
final_project.py: The main program file containing all logic.
word_list.txt (optional): A text file containing words for the Hangman game.
Results files:
username_ocean_results.txt: Stores OCEAN Personality Test results.
Other quizzes do not save results to files.
Future Enhancements
Add multiplayer functionality for Tic-Tac-Toe.
Store results for all quizzes in files for long-term tracking.
Include more diverse questions and categories in quizzes.
Credits
Author: Jeff Loula
Tools Used: Python (Random module, File I/O, Exception Handling)