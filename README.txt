Overview
This project is a comprehensive game hub created in Python, featuring several engaging activities and quizzes designed for educational and entertainment purposes. Users can log in, select a game from the menu, and enjoy a variety of challenges. The application supports tracking scores and provides detailed feedback for the quizzes.

Features
1. Login System
Users are greeted with a login screen where they input their username.
The system personalizes their experience with their name.
2. Game Menu
A menu-driven system allows users to select from the following options:
Hangman: A word-guessing game with limited attempts.
Tic-Tac-Toe: A classic game played against the computer.
Math Quiz: A customizable difficulty quiz testing arithmetic and algebra skills.
OCEAN Personality Test: A comprehensive test to calculate personality scores based on the OCEAN model.
Periodic Table Quiz: Tests the knowledge of chemical elements.
States and Capitals Quiz: Checks knowledge of U.S. states and their capitals.
Amendments Quiz: Tests knowledge of U.S. Constitutional Amendments.
Exit: Allows users to exit the program.
Game Details
Hangman
Guess the letters of a randomly selected word within 6 attempts.
Tracks previously guessed letters and provides feedback for correct and incorrect guesses.
Tic-Tac-Toe
Classic game of strategy played against the computer.
The program ensures fairness and tries to block the user's winning moves.
Math Quiz
Difficulty levels: Easy, Medium, and Hard.
Randomly generates problems involving addition, subtraction, multiplication, division, and basic algebra.
Tracks the user's score and provides detailed results at the end.
OCEAN Personality Test
A 50-question test to evaluate personality traits: Openness, Conscientiousness, Extroversion, Agreeableness, and Neuroticism.
Displays results with descriptions and saves them to a file for review.
Periodic Table Quiz
Randomly selects elements from the periodic table and asks users to identify their symbols or names.
Ends after 10 wrong answers, tracking correct responses.
States and Capitals Quiz
Questions about matching states to their capitals or vice versa.
Tracks correct and incorrect answers.
Amendments Quiz
Tests knowledge of U.S. Constitutional Amendments.
Presents descriptions and asks users to identify the corresponding amendment number.
Installation and Usage
Prerequisites
Python 3.x
No additional libraries are required; the code runs on the standard Python library.
Running the Program
Download the PythonFinal-Final.py file.
Open your terminal or command prompt.
Navigate to the directory containing the file.
Run the program using:
python PythonFinal-Final.py
Follow the prompts to log in and select your desired game from the menu.
File Outputs
Quizzes save results to uniquely named text files in the same directory as the program.
Example:
username_ocean_results.txt for the OCEAN Personality Test.
username_math_quiz_results.txt for the Math Quiz.
Development Notes
The program is modular, making it easy to add new games or extend existing features.
Error handling ensures robustness, guiding users with clear messages for invalid inputs.
The program maintains a user-friendly interface with a clear and structured menu.
Future Enhancements
Add a graphical user interface (GUI) for a more interactive experience.
Expand quizzes with additional categories and difficulty levels.
Implement a leaderboard for competitive play.
Author
Jeff Loula
This project was developed as part of a final assignment to demonstrate Python programming skills.
License
This project is open source and free for educational purposes.
