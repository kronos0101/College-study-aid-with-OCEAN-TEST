#Python Final Project
## Jeff Loula

import os
from datetime import datetime
import random

# Function to print "GET READY TO GAME"
def print_game_message():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
    print(" GGGG  EEEEE TTTTT      RRRR  EEEEE    A    DDDD  Y   Y")
    print("G      E       T        R   R E       A A   D   D  Y Y")
    print("G GGG  EEEE    T        RRRR  EEEE   AAAAA  D   D   Y")
    print("G   G  E       T        R  R  E     A     A D   D   Y")
    print(" GGGG  EEEEE   T        R   R EEEEE A     A DDDD    Y")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
    print("     TTTTT OOO     GGGG     A     M   M  EEEEE")
    print("       T  O   O   G        A A    MM MM  E    ")
    print("       T  O   O   G   GG  AAAAA  M  M  M EEEE ")
    print("       T  O   O   G    G A     A M     M E    ")
    print("       T   OOO     GGGG  A     A M     M EEEEE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print_game_message()
# Login Function
def login():
    print("Welcome! Please log in.")
    name = input("Enter a user name: ")
    print(f"Hello, {name}! Let's start the game.")
    return name

# Game Menu Function
def game_menu():
    while True:
        try:
            print("\nGame Menu:")
            print("1. Hangman")
            print("2. Tic-Tac-Toe (Against Computer)")
            print("3. Math Quiz")
            print("4. OCEAN Personality Test")
            print("5. Periodic Table Quiz")
            print("6. USA States and Capitals Quiz")
            print("7. Amendments Quiz")
            print("8. Exit")
            choice = int(input("Select a game (1-8): "))
            if choice < 1 or choice > 8:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")

# Hangman Game
def hangman():
    word_list = ['python', 'hangman', 'challenge', 'programming', 'game', 'computer', 'learn', 'question', 'program', 'processor', 'algorithm', 'binary', 'compile', 'debug', 'function', 'hardware', 'internet', 'javascript', 'keyboard', 'loop', 'memory', 'network', 'object', 'parameter', 'query', 'software', 'syntax', 'variable', 'website', 'xml', 'java', 'method', 'operation', 'protocol', 'script', 'server', 'terminal', 'utility', 'virtual', 'database', 'array', 'bit', 'cache', 'data', 'domain', 'encryption', 'firewall', 'gateway', 'hash', 'interface', 'jupyter', 'kernel', 'lambda', 'machine', 'node', 'path', 'recurse', 'stack', 'thread', 'unicode', 'vector', 'while', 'xcode', 'yield', 'zip', 'docker', 'environment', 'flask', 'git', 'host', 'index', 'json', 'key', 'log', 'module', 'numpy', 'operand', 'packet', 'queue', 'register', 'socket', 'tuple', 'unix', 'virtualenv', 'print', 'input', 'len', 'range', 'type', 'int', 'float', 'str', 'list', 'dict', 'set', 'abs', 'sum', 'max', 'min', 'round', 'sorted', 'reversed', 'enumerate', 'map', 'filter', 'reduce', 'all', 'any', 'open', 'close', 'read', 'write', 'append', 'split', 'join', 'replace', 'format', 'find', 'strip', 'pop', 'remove', 'insert', 'count', 'extend', 'copy', 'clear', 'keys', 'values', 'items', 'get', 'update', 'has_key', 'fromkeys', 'setdefault', 'isinstance', 'issubclass', 'id', 'hex', 'oct', 'bin', 'ord', 'chr', 'divmod', 'pow', 'next', 'iter', 'dir', 'globals', 'locals', 'exec', 'eval', 'help', 'API', 'Bitwise', 'Class', 'Cloud', 'CLI', 'Concurrent', 'Constructor', 'Cybersecurity', 'Daemon', 'Dataframe', 'Decorator', 'Decryption', 'Dependency', 'DevOps', 'Exception', 'Framework', 'GPU', 'IDE', 'Immutable', 'Inheritance', 'Integration', 'Latency', 'Library', 'Multithreading', 'Namespace', 'Open-source', 'Overloading', 'Parsing', 'Pipeline', 'Polymorphism', 'Refactor', 'Regression', 'Repository', 'RESTful', 'SDK', 'Serialization', 'Singleton', 'Sprint', 'Subroutine', 'Swagger', 'TCP/IP', 'Thunk', 'Token', 'Unit test', 'Version control', 'Webhook', 'WebSocket', 'YAML', 'Zero-day', 'Zoom'
]
    word = random.choice(word_list)
    guessed_letters = []
    attempts = 6
    guessed_word = ['_'] * len(word)
    print("Welcome to Hangman!")
    while attempts > 0:
        print("\nWord: " + ' '.join(guessed_word))
        print(f"You have {attempts} attempts left.")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1
        if '_' not in guessed_word:
            print("\nCongratulations! You guessed the word: " + word)
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Tic-Tac-Toe Game (Against Computer)
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

def computer_move(board):
    available_moves = get_available_moves(board)
    
    # Check if the computer can win in the next move
    for move in available_moves:
        board[move] = 'O'
        if check_winner(board, 'O'):
            return move
        board[move] = ' '
    
    # Check if the player can win in the next move and block them
    for move in available_moves:
        board[move] = 'X'
        if check_winner(board, 'X'):
            return move
        board[move] = ' '
    
    # Otherwise, pick the center if available
    if board[4] == ' ':
        return 4
    
    # If center is not available, choose a random move
    return random.choice(available_moves)

def tic_tac_toe():
    board = [' '] * 9
    player = 'X'  # Human player
    computer = 'O'  # Computer player
    
    while True:
        print_board(board)
        # Player's turn
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = player
        else:
            print("Invalid move, try again.")
            continue
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~  ~~~~~  ~~~~~~~~~~~~~~~~~~~~  ~~~~~~  ~~~~~~~  ~   ~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~ ~~~ ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~ ~ ~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~  ~~~  ~~~~~ ~~~~ ~~~ ~~~ ~~~~~ ~~~~    ~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~  ~~  ~~~~ ~~~ ~~~~~~~ ~~ ~~~~~ ~ ~~~~~~ ~~~ ~~~~ ~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~~~   ~~~~~~~~~  ~~~~~~  ~~~~~~~ ~~~ ~~~~ ~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        if not get_available_moves(board):
            print_board(board)
            print("It's a draw!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~  ~~~~~  ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~ ~~~ ~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~  ~~     ~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~  ~~~  ~~~ ~~~~~~~  ~~~~ ~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~  ~~  ~~~~ ~~~ ~~~~ ~~~~~  ~~  ~~~~ ~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~~~   ~~~~~    ~~~~  ~~~~  ~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        # Computer's turn
        comp_move = computer_move(board)
        board[comp_move] = computer
        print(f"\nComputer (O) placed at position {comp_move + 1}.")
        if check_winner(board, computer):
            print_board(board)
            print(f"Computer ({computer}) wins!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~  ~~~~~  ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~ ~~~ ~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~  ~~     ~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~  ~~~  ~~~ ~~~~~~~  ~~~~ ~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~  ~~  ~~~~ ~~~ ~~~~ ~~~~~  ~~  ~~~~ ~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~~~   ~~~~~    ~~~~  ~~~~  ~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
        if not get_available_moves(board):
            print_board(board)
            print("It's a draw!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~  ~~~~~  ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~ ~~~ ~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~  ~~     ~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~  ~~~  ~~~ ~~~~~~~  ~~~~ ~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~  ~~  ~~~~ ~~~ ~~~~ ~~~~~  ~~  ~~~~ ~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~ ~~~~~~~  ~~~~~~~   ~~~~~    ~~~~  ~~~~  ~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break
# OCEAN Personality Test
def ocean_test():
    print("Welcome to the Personality Test!")
    print("Please rate each statement on a scale of 1 (Strongly Disagree) to 5 (Strongly Agree).")
    
    # Define questions
    questions = [
        "1. Am the life of the party.",
        "2. Feel little concern for others.",
        "3. Am always prepared.",
        "4. Get stressed out easily.",
        "5. Have a rich vocabulary.",
        "6. Don't talk a lot.",
        "7. Am interested in people.",
        "8. Leave my belongings around.",
        "9. Am relaxed most of the time.",
        "10. Have difficulty understanding abstract ideas.",
        "11. Feel comfortable around people.",
        "12. Insult people.",
        "13. Pay attention to details.",
        "14. Worry about things.",
        "15. Have a vivid imagination.",
        "16. Keep in the background.",
        "17. Sympathize with others' feelings.",
        "18. Make a mess of things.",
        "19. Seldom feel blue.",
        "20. Am not interested in abstract ideas.",
        "21. Start conversations.",
        "22. Am not interested in other people's problems.",
        "23. Get chores done right away.",
        "24. Am easily disturbed.",
        "25. Have excellent ideas.",
        "26. Have little to say.",
        "27. Have a soft heart.",
        "28. Often forget to put things back in their proper place.",
        "29. Get upset easily.",
        "30. Do not have a good imagination.",
        "31. Talk to a lot of different people at parties.",
        "32. Am not really interested in others.",
        "33. Like order.",
        "34. Change my mood a lot.",
        "35. Am quick to understand things.",
        "36. Don't like to draw attention to myself.",
        "37. Take time out for others.",
        "38. Shirk my duties.",
        "39. Have frequent mood swings.",
        "40. Use difficult words.",
        "41. Don't mind being the center of attention.",
        "42. Feel others' emotions.",
        "43. Follow a schedule.",
        "44. Get irritated easily.",
        "45. Spend time reflecting on things.",
        "46. Am quiet around strangers.",
        "47. Make people feel at ease.",
        "48. Am exacting in my work.",
        "49. Often feel blue.",
        "50. Am full of ideas."
    ]

    # Get user's name
    name = input("Please enter your name: ")

    # Get ratings from user
    ratings = []
    for question in questions:
        while True:
            try:
                rating = int(input(f"{question} (1-5): "))
                if rating < 1 or rating > 5:
                    raise ValueError
                ratings.append(rating)
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    # Calculate scores
    E = 20 + (ratings[0] - ratings[5] + ratings[10] - ratings[15] + ratings[20] - ratings[25] +
              ratings[30] - ratings[35] + ratings[40] - ratings[45])
    A = 14 + (ratings[6] - ratings[1] + ratings[11] - ratings[16] + ratings[21] - ratings[26] +
              ratings[31] - ratings[36] + ratings[41] - ratings[46])
    C = 14 + (ratings[2] - ratings[7] + ratings[12] - ratings[17] + ratings[22] - ratings[27] +
              ratings[32] - ratings[37] + ratings[42] - ratings[47])
    N = 38 - (ratings[3] - ratings[8] + ratings[13] - ratings[18] + ratings[23] - ratings[28] +
              ratings[33] - ratings[38] + ratings[43] - ratings[48])
    O = 8 + (ratings[4] - ratings[9] + ratings[14] - ratings[19] + ratings[24] - ratings[29] +
             ratings[34] + ratings[39] + ratings[44] + ratings[49])

    # Create a results string
    results = (
        f"Openness to Experience (O): {O}\n"
        f"Conscientiousness (C): {C}\n"
        f"Extroversion (E): {E}\n"
        f"Agreeableness (A): {A}\n"
        f"Neuroticism (N): {N}\n"
    )
    # Display results
    print("\nYour Personality Scores:")
    print(results)

    # Save results to file in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sanitized_name = "".join(c for c in name if c.isalnum() or c in " _-").strip()  # Clean name for filename
    filename = os.path.join(script_dir, f"{sanitized_name}_ocean_results.txt")

    with open(filename, "w") as file:
        file.write(f"Personality Test Results for {name}:\n\n")
        file.write(results)
        file.write("https://openpsychometrics.org/tests/IPIP-BFFM/results.php")
    
    print(f"\nYour results have been saved in the file: {filename}")
    print ("https://openpsychometrics.org/tests/IPIP-BFFM/results.php")

## Math Game
import os
from datetime import datetime
import random

def math_quiz():
    print("Welcome to the Math Quiz!")
    name = input("Enter your name: ").strip()
    
    # Validate difficulty level input
    while True:
        try:
            difficulty = int(input("Select difficulty level (1 - Easy, 2 - Medium, 3 - Hard): "))
            if difficulty not in [1, 2, 3]:
                raise ValueError("Difficulty must be 1, 2, or 3.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    score = 0
    operations = ['+', '-', '*', '/', 'algebra']
    results = []

    # Number of questions
    num_questions = 5
    for i in range(1, num_questions + 1):
        # Generate random numbers based on difficulty level
        if difficulty == 1:  # Easy
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif difficulty == 2:  # Medium
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
        else:  # Hard
            num1 = random.randint(50, 200)
            num2 = random.randint(50, 200)

        operation = random.choice(operations)

        # Generate a question and the correct answer
        if operation == '+':
            correct_answer = num1 + num2
            question = f"What is {num1} + {num2}?"
        elif operation == '-':
            correct_answer = num1 - num2
            question = f"What is {num1} - {num2}?"
        elif operation == '*':
            correct_answer = num1 * num2
            question = f"What is {num1} * {num2}?"
        elif operation == '/':
            num1 = num1 * num2  # Ensure num1 is a multiple of num2 for integer division
            correct_answer = num1 // num2
            question = f"What is {num1} / {num2} (integer division)?"
        elif operation == 'algebra':
            x = random.randint(1, 10)
            coefficient = random.randint(1, 10)
            constant = random.randint(1, 10)
            num2 = coefficient * x + constant
            correct_answer = x
            question = f"Solve for x: {coefficient}x + {constant} = {num2}"

        # Display question and get user answer
        print(f"\nQuestion {i}: {question}")
        while True:
            try:
                answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input! Please enter a whole number.")

        # Check if the answer is correct
        if answer == correct_answer:
            print("Correct!")
            score += 1
            results.append(f"Question {i}: {question} - Your Answer: {answer} - Correct")
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            results.append(f"Question {i}: {question} - Your Answer: {answer} - Correct Answer: {correct_answer}")

    # Display the final score
    print(f"\nYour total score is {score}/{num_questions}.")
    results.append(f"Final Score: {score}/{num_questions}")

    # Display the detailed results
    print("\nDetailed Results:")
    for result in results:
        print(result)

    # Save the results to a file named after the player
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sanitized_name = "".join(c for c in name if c.isalnum() or c in " _-").strip()  # Clean the name for a valid filename
    filename = os.path.join(script_dir, f"{sanitized_name}_math_quiz_results.txt")

    # Save the results to a file
    with open(filename, "w") as file:
        file.write(f"Math Quiz Results for {name}\n")
        file.write(f"Score: {score}/{num_questions}\n\n")
        file.write("Detailed Results:\n")
        for result in results:
            file.write(f"{result}\n")
    
    print(f"\nYour results have been saved in the file: {filename}")
    print("Thank you for playing the Math Quiz!")

### Periodic table quiz
def periodic_table_quiz():
    # Dictionary of elements with their symbols as keys and names as values
    elements = {
    "H": "Hydrogen (1) \n  Family: Nonmetal \n Electron Configuration: 1s1",
    "He": "Helium (2) \n Family: Noble Gas \v Electron Configuration: 1s2",
    "Li": "Lithium (3) \nFamily: Alkali Metal \nElectron Configuration: [He] 2s1",
    "Be": "Beryllium (4) \nFamily: Alkaline Earth Metal \nElectron Configuration: [He] 2s2",
    "B": "Boron (5) \nFamily: Metalloid \nElectron Configuration: [He] 2s2 2p1",
    "C": "Carbon (6) \nFamily: Nonmetal \nElectron Configuration: [He] 2s2 2p2",
    "N": "Nitrogen (7) \nFamily: Nonmetal \nElectron Configuration: [He] 2s2 2p3",
    "O": "Oxygen (8) \nFamily: Nonmetal \nElectron Configuration: [He] 2s2 2p4",
    "F": "Fluorine (9) \nFamily: Halogen \nElectron Configuration: [He] 2s2 2p5",
    "Ne": "Neon (10) \nFamily: Noble Gas \nElectron Configuration: [He] 2s2 2p6",
    "Na": "Sodium (11) \nFamily: Alkali Metal \nElectron Configuration: [Ne] 3s1",
    "Mg": "Magnesium (12) \nFamily: Alkaline Earth Metal \nElectron Configuration: [Ne] 3s2",
    "Al": "Aluminum (13) \nFamily: Post-Transition Metal \nElectron Configuration: [Ne] 3s2 3p1",
    "Si": "Silicon (14) \nFamily: Metalloid \nElectron Configuration: [Ne] 3s2 3p2",
    "P": "Phosphorus (15) \nFamily: Nonmetal \nElectron Configuration: [Ne] 3s2 3p3",
    "S": "Sulfur (16) \nFamily: Nonmetal \nElectron Configuration: [Ne] 3s2 3p4",
    "Cl": "Chlorine (17) \nFamily: Halogen \nElectron Configuration: [Ne] 3s2 3p5",
    "Ar": "Argon (18) \nFamily: Noble Gas \nElectron Configuration: [Ne] 3s2 3p6",
    "K": "Potassium (19) \nFamily: Alkali Metal \nElectron Configuration: [Ar] 4s1",
    "Ca": "Calcium (20) \nFamily: Alkaline Earth Metal \nElectron Configuration: [Ar] 4s2",
    "Sc": "Scandium (21) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d1 4s2",
    "Ti": "Titanium (22) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d2 4s2",
    "V": "Vanadium (23) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d3 4s2",
    "Cr": "Chromium (24) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d5 4s1",
    "Mn": "Manganese (25) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d5 4s2",
    "Fe": "Iron (26) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d6 4s2",
    "Co": "Cobalt (27) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d7 4s2",
    "Ni": "Nickel (28) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d8 4s2",
    "Cu": "Copper (29) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d10 4s1",
    "Zn": "Zinc (30) \nFamily: Transition Metal \nElectron Configuration: [Ar] 3d10 4s2",
    "Ga": "Gallium (31) \nFamily: Post-Transition Metal \nElectron Configuration: [Ar] 3d10 4s2 4p1",
    "Ge": "Germanium (32) \nFamily: Metalloid \nElectron Configuration: [Ar] 3d10 4s2 4p2",
    "As": "Arsenic (33) \nFamily: Metalloid \nElectron Configuration: [Ar] 3d10 4s2 4p3",
    "Se": "Selenium (34) \nFamily: Nonmetal \nElectron Configuration: [Ar] 3d10 4s2 4p4",
    "Br": "Bromine (35) \nFamily: Halogen \nElectron Configuration: [Ar] 3d10 4s2 4p5",
    "Kr": "Krypton (36) \nFamily: Noble Gas \nElectron Configuration: [Ar] 3d10 4s2 4p6",
    "Rb": "Rubidium (37) \nFamily: Alkali Metal \nElectron Configuration: [Kr] 5s1",
    "Sr": "Strontium (38) \nFamily: Alkaline Earth Metal \nElectron Configuration: [Kr] 5s2",
    "Y": "Yttrium (39) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d1 5s2",
    "Zr": "Zirconium (40) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d2 5s2",
    "Nb": "Niobium (41) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d4 5s1",
    "Mo": "Molybdenum (42) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d5 5s1",
    "Tc": "Technetium (43) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d5 5s2",
    "Ru": "Ruthenium (44) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d7 5s1",
    "Rh": "Rhodium (45) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d8 5s1",
    "Pd": "Palladium (46) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d10",
    "Ag": "Silver (47) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d10 5s1",
    "Cd": "Cadmium (48) \nFamily: Transition Metal \nElectron Configuration: [Kr] 4d10 5s2",
    "In": "Indium (49) \nFamily: Post-Transition Metal \nElectron Configuration: [Kr] 4d10 5s2 5p1",
    "Sn": "Tin (50) \nFamily: Post-Transition Metal \nElectron Configuration: [Kr] 4d10 5s2 5p2",
    "Sb": "Antimony (51) \nFamily: Metalloid \nElectron Configuration: [Kr] 4d10 5s2 5p3",
    "Te": "Tellurium (52) \nFamily: Metalloid \nElectron Configuration: [Kr] 4d10 5s2 5p4",
    "I": "Iodine (53) \nFamily: Halogen \nElectron Configuration: [Kr] 4d10 5s2 5p5",
    "Xe": "Xenon (54) \nFamily: Noble Gas \nElectron Configuration: [Kr] 4d10 5s2 5p6",
    "Cs": "Cesium (55) \nFamily: Alkali Metal \nElectron Configuration: [Xe] 6s1",
    "Ba": "Barium (56) \nFamily: Alkaline Earth Metal \nElectron Configuration: [Xe] 6s2",
    "La": "Lanthanum (57) \nFamily: Lanthanide \nElectron Configuration: [Xe] 5d1 6s2",
    "Ce": "Cerium (58) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f1 5d1 6s2",
    "Pr": "Praseodymium (59) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f3 6s2",
    "Nd": "Neodymium (60) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f4 6s2",
    "Pm": "Promethium (61) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f5 6s2",
    "Sm": "Samarium (62) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f6 6s2",
    "Eu": "Europium (63) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f7 6s2",
    "Gd": "Gadolinium (64) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f7 5d1 6s2",
    "Tb": "Terbium (65) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f9 6s2",
    "Dy": "Dysprosium (66) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f10 6s2",
    "Ho": "Holmium (67) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f11 6s2",
    "Er": "Erbium (68) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f12 6s2",
    "Tm": "Thulium (69) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f13 6s2",
    "Yb": "Ytterbium (70) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f14 6s2",
    "Lu": "Lutetium (71) \nFamily: Lanthanide \nElectron Configuration: [Xe] 4f14 5d1 6s2",
    "Hf": "Hafnium (72) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d2 6s2",
    "Ta": "Tantalum (73) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d3 6s2",
    "W": "Tungsten (74) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d4 6s2",
    "Re": "Rhenium (75) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d5 6s2",
    "Os": "Osmium (76) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d6 6s2",
    "Ir": "Iridium (77) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d7 6s2",
    "Pt": "Platinum (78) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d9 6s1",
    "Au": "Gold (79) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d10 6s1",
    "Hg": "Mercury (80) \nFamily: Transition Metal \nElectron Configuration: [Xe] 4f14 5d10 6s2",
    "Tl": "Thallium (81) \nFamily: Post-Transition Metal \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p1",
    "Pb": "Lead (82) \nFamily: Post-Transition Metal \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p2",
    "Bi": "Bismuth (83) \nFamily: Post-Transition Metal \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p3",
    "Po": "Polonium (84) \nFamily: Metalloid \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p4",
    "At": "Astatine (85) \nFamily: Metalloid \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p5",
    "Rn": "Radon (86) \nFamily: Noble Gas \nElectron Configuration: [Xe] 4f14 5d10 6s2 6p6",
    "Fr": "Francium (87) \nFamily: Alkali Metal \nElectron Configuration: [Rn] 7s1",
    "Ra": "Radium (88) \nFamily: Alkaline Earth Metal \nElectron Configuration: [Rn] 7s2",
    "Ac": "Actinium (89) \nFamily: Actinide \nElectron Configuration: [Rn] 6d1 7s2",
    "Th": "Thorium (90) \nFamily: Actinide \nElectron Configuration: [Rn] 6d2 7s2",
    "Pa": "Protactinium (91) \nFamily: Actinide \nElectron Configuration: [Rn] 5f2 6d1 7s2",
    "U": "Uranium (92) \nFamily: Actinide \nElectron Configuration: [Rn] 5f3 6d1 7s2",
    "Np": "Neptunium (93) \nFamily: Actinide \nElectron Configuration: [Rn] 5f4 6d1 7s2",
    "Pu": "Plutonium (94) \nFamily: Actinide \nElectron Configuration: [Rn] 5f6 7s2",
    "Am": "Americium (95) \nFamily: Actinide \nElectron Configuration: [Rn] 5f7 7s2",
    "Cm": "Curium (96) \nFamily: Actinide \nElectron Configuration: [Rn] 5f7 6d1 7s2",
    "Bk": "Berkelium (97) \nFamily: Actinide \nElectron Configuration: [Rn] 5f9 7s2",
    "Cf": "Californium (98) \nFamily: Actinide \nElectron Configuration: [Rn] 5f10 7s2",
    "Es": "Einsteinium (99) \nFamily: Actinide \nElectron Configuration: [Rn] 5f11 7s2",
    "Fm": "Fermium (100) \nFamily: Actinide \nElectron Configuration: [Rn] 5f12 7s2",
    "Md": "Mendelevium (101) \nFamily: Actinide \nElectron Configuration: [Rn] 5f13 7s2",
    "No": "Nobelium (102) \nFamily: Actinide \nElectron Configuration: [Rn] 5f14 7s2",
    "Lr": "Lawrencium (103) \nFamily: Actinide \nElectron Configuration: [Rn] 5f14 7s2 7p1",
    "Rf": "Rutherfordium (104) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d2 7s2",
    "Db": "Dubnium (105) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d3 7s2",
    "Sg": "Seaborgium (106) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6", 
    "Bh": "Bohrium (107) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d5 7s2", "Hs": "Hassium (108) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d6 7s2", "Mt": "Meitnerium (109) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d7 7s2", "Ds": "Darmstadtium (110) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d9 7s1", "Rg": "Roentgenium (111) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s1", "Cn": "Copernicium (112) \nFamily: Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s2", "Nh": "Nihonium (113) \nFamily: Post-Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p1", "Fl": "Flerovium (114) \nFamily: Post-Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p2", "Mc": "Moscovium (115) \nFamily: Post-Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p3", "Lv": "Livermorium (116) \nFamily: Post-Transition Metal \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p4", "Ts": "Tennessine (117) \nFamily: Halogen \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p5", "Og": "Oganesson (118) \nFamily: Noble Gas \nElectron Configuration: [Rn] 5f14 6d10 7s2 7p6",
	
   }
   
    name = input("Enter your name: ").strip()
    correct = 0
    wrong = 0
    asked = set()
    all_questions = list(elements.items())

    print("\nWelcome to the Periodic Table Quiz!")
    print("You will answer questions until you get 10 wrong answers.")

    while wrong < 10:
        if len(asked) == len(all_questions):  # Reset if all questions have been asked
            print("\nYou've gone through all the elements. Repeating questions now.")
            asked.clear()

        while True:
            symbol, element_description = random.choice(all_questions)
            if symbol not in asked:
                asked.add(symbol)
                break

        answer = input(f"What is the symbol for this element?\nDescription: {element_description}\nYour answer: ").strip().title()
        if answer == symbol:
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong! The correct answer is {symbol}.")
            wrong += 1

        print(f"Correct: {correct}, Wrong: {wrong}/10")

    print(f"\nGame over! You answered {correct} questions correctly before getting 10 wrong.")
#amendments-quiz 
def amendments_quiz():
    # Simple format for questions
    questions = {
    1: "Summary: Freedom of speech, religion, press, assembly, and petition \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: All U.S. citizens, especially activists and minorities.\n",
    2: "Summary: Right to keep and bear arms \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Gun owners and advocates for self-defense.\n",
    3: "Summary: No quartering of soldiers in private homes without consent \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Private homeowners.\n",
    4: "Summary: Protection against unreasonable searches and seizures \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Individuals involved in legal or criminal justice matters.\n",
    5: "Summary: Protection against self-incrimination, double jeopardy; guarantees due process \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Defendants in criminal cases.\n",
    6: "Summary: Right to a speedy and public trial by an impartial jury \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Defendants in criminal trials.\n",
    7: "Summary: Right to trial by jury in civil cases \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Civil litigants seeking justice.\n",
    8: "Summary: Protection against cruel and unusual punishment \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: Inmates and criminal defendants.\n",
    9: "Summary: Rights retained by the people, even if not specifically enumerated in the Constitution \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: All U.S. citizens, especially those concerned about overreach.\n",
    10: "Summary: Powers not delegated to the federal government are reserved to the states or the people \nDate ratified: (1791) \nPrimary Supporter: James Madison \nMost impacted: State governments and individuals.\n",
    11: "Summary: Limits lawsuits against states \nDate ratified: (1795) \nPrimary Supporter: John Marshall \nMost impacted: State governments.\n",
    12: "Summary: Revises presidential election procedures \nDate ratified: (1804) \nPrimary Supporter: Thomas Jefferson \nMost impacted: Presidential candidates and voters.\n",
    13: "Summary: Abolition of slavery \nDate ratified: (1865) \nPrimary Supporter: Abraham Lincoln \nMost impacted: Enslaved individuals.\n",
    14: "Summary: Equal protection under the law and due process for all citizens \nDate ratified: (1868) \nPrimary Supporter: John Bingham \nMost impacted: Minorities and historically marginalized groups.\n",
    15: "Summary: Right to vote cannot be denied based on race, color, or previous servitude \nDate ratified: (1870) \nPrimary Supporter: Ulysses S. Grant \nMost impacted: African Americans and minorities.\n",
    16: "Summary: Congress can levy an income tax \nDate ratified: (1913) \nPrimary Supporter: William Howard Taft \nMost impacted: Taxpayers.\n",
    17: "Summary: Establishes the direct election of U.S. Senators by popular vote \nDate ratified: (1913) \nPrimary Supporter: Woodrow Wilson \nMost impacted: Voters.\n",
    18: "Summary: Prohibition of alcohol \nDate ratified: (1919, repealed by the 21st Amendment in 1933) \nPrimary Supporter: Wayne Wheeler \nMost impacted: Alcohol producers and consumers.\n",
    19: "Summary: Women's right to vote \nDate ratified: (1920) \nPrimary Supporter: Susan B. Anthony \nMost impacted: Women.\n",
    20: "Summary: Changes the dates of congressional and presidential terms \nDate ratified: (1933) \nPrimary Supporter: George Norris \nMost impacted: Congress and the president.\n",
    21: "Summary: Repeal of Prohibition (18th Amendment) \nDate ratified: (1933) \nPrimary Supporter: Fiorello La Guardia \nMost impacted: Alcohol producers and consumers.\n",
    22: "Summary: Limits the President to two terms in office \nDate ratified: (1951) \nPrimary Supporter: Harry S. Truman \nMost impacted: Presidential candidates.\n",
    23: "Summary: Gives residents of Washington D.C. the right to vote for representatives in the Electoral College \nDate ratified: (1961) \nPrimary Supporter: Eleanor Holmes Norton \nMost impacted: D.C. residents.\n",
    24: "Summary: Abolishes poll taxes \nDate ratified: (1964) \nPrimary Supporter: Lyndon B. Johnson \nMost impacted: Low-income voters.\n",
    25: "Summary: Addresses presidential succession and disability \nDate ratified: (1967) \nPrimary Supporter: Birch Bayh \nMost impacted: Presidential officeholders and their staff.\n",
    26: "Summary: Voting age lowered to 18 \nDate ratified: (1971) \nPrimary Supporter: Jennings Randolph \nMost impacted: Young voters.\n",
    27: "Summary: Delays laws affecting Congressional salary from taking effect until after the next election of representatives \nDate ratified: (1992) \nPrimary Supporter: Gregory Watson \nMost impacted: Members of Congress.\n"
}


    # Detailed answers
    answers = {
        1: "Freedom of speech, religion, press, assembly, and petition (1791) - James Madison - Most impacted: All U.S. citizens, especially activists and minorities. Trick: 1 mouth, 1 voice.",
        2: "Right to keep and bear arms (1791) - James Madison - Most impacted: Gun owners and advocates for self-defense. Trick: 2 arms to bear arms.",
        3: "No quartering of soldiers in private homes without consent (1791) - James Madison - Most impacted: Private homeowners. Trick: 3's a crowd (no soldiers in homes).",
        4: "Protection against unreasonable searches and seizures (1791) - James Madison - Most impacted: Individuals involved in legal or criminal justice matters. Trick: 4 walls protect your privacy.",
        5: "Protection against self-incrimination, double jeopardy; guarantees due process (1791) - James Madison - Most impacted: Defendants in criminal cases. Trick: Take the 5th (remain silent).",
        6: "Right to a speedy and public trial by an impartial jury (1791) - James Madison - Most impacted: Defendants in criminal trials. Trick: Speedy trial gets you home by 6.",
        7: "Right to trial by jury in civil cases (1791) - James Madison - Most impacted: Civil litigants seeking justice. Trick: 7 rhymes with 'heaven'—fair civil trials.",
        8: "Protection against cruel and unusual punishment (1791) - James Madison - Most impacted: Inmates and criminal defendants. Trick: Sideways 8 looks like handcuffs.",
        9: "Rights retained by the people, even if not specifically enumerated in the Constitution (1791) - James Madison - Most impacted: All U.S. citizens, especially those concerned about overreach. Trick: 9 makes sure you’re fine.",
        10: "Powers not delegated to the federal government are reserved to the states or the people (1791) - James Madison - Most impacted: State governments and individuals. Trick: Federal power ends at 10.",
        11: "Limits lawsuits against states (1795) - John Marshall - Most impacted: State governments. Trick: 1-on-1 disputes between citizens and states.",
        12: "Revises presidential election procedures (1804) - Thomas Jefferson - Most impacted: Presidential candidates and voters. Trick: 1 vote for president, 2 for VP.",
        13: "Abolition of slavery (1865) - Abraham Lincoln - Most impacted: Enslaved individuals. Trick: Unlucky 13 turned lucky for freedom.",
        14: "Equal protection under the law and due process for all citizens (1868) - John Bingham - Most impacted: Minorities and historically marginalized groups. Trick: 1 nation 4 equality.",
        15: "Right to vote cannot be denied based on race, color, or previous servitude (1870) - Ulysses S. Grant - Most impacted: African Americans and minorities. Trick: 15 freed votes.",
        16: "Congress can levy an income tax (1913) - William Howard Taft - Most impacted: Taxpayers. Trick: Sweet 16, but now you pay taxes.",
        17: "Establishes the direct election of U.S. Senators by popular vote (1913) - Woodrow Wilson - Most impacted: Voters. Trick: 17 senators closer to heaven (elected by people).",
        18: "Prohibition of alcohol (repealed by the 21st Amendment) (1919) - Wayne Wheeler - Most impacted: Alcohol producers and consumers. Trick: 18 is too young to drink.",
        19: "Women's right to vote (1920) - Susan B. Anthony - Most impacted: Women. Trick: 19 suffragettes on the march.",
        20: "Changes the dates of congressional and presidential terms (1933) - George Norris - Most impacted: Congress and the president. Trick: Jan 20 starts a new term.",
        21: "Repeal of Prohibition (18th Amendment) (1933) - Fiorello La Guardia - Most impacted: Alcohol producers and consumers. Trick: 21 means you can drink.",
        22: "Limits the President to two terms in office (1951) - Harry S. Truman - Most impacted: Presidential candidates. Trick: 2 terms for 22.",
        23: "Gives residents of Washington D.C. the right to vote for representatives in the Electoral College (1961) - Eleanor Holmes Norton - Most impacted: D.C. residents. Trick: 2-3 votes for D.C.",
        24: "Abolishes poll taxes (1964) - Lyndon B. Johnson - Most impacted: Low-income voters. Trick: 24 stops taxing at the door.",
        25: "Addresses presidential succession and disability (1967) - Birch Bayh - Most impacted: Presidential officeholders and their staff. Trick: 25 keeps the presidency alive.",
        26: "Voting age lowered to 18 (1971) - Jennings Randolph - Most impacted: Young voters. Trick: 2+6 = 18 to vote.",
        27: "Delays laws affecting Congressional salary from taking effect until after the next election of representatives (1992) - Gregory Watson - Most impacted: Members of Congress. Trick: 27 waits till the next election."
    }

    score = 0
    print("\nWelcome to the Amendments Quiz!")
    print("You will be given 10 descriptions of amendments. Your task is to enter the amendment number that matches the description.\n")
    
    for _ in range(10):  # Ask 10 random questions
        amendment, description = random.choice(list(questions.items()))
        try:
            answer = int(input(f"Which amendment is described as:\n\"{description}enter the amendment number: "))
            if answer == amendment:
                print("Correct!")
                print("\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is Amendment {amendment}.")
                print(f"Details: {answers[amendment]}")
                print("\n")
        except ValueError:
            print("Invalid input! Please enter a number.")
            print("\n")
            

    print(f"\nYour final score: {score}/10")
    if score == 10:
        print("Excellent! You know your amendments well!")
        print("\n")
                
    elif score >= 7:
        print("Good job! A little more study and you'll be a pro.")
        print("\n")
                
    else:
        print("Keep learning! The Constitution is worth knowing.")
        print("\n")
                
def states_capitals_quiz():
    
    # Dictionary of U.S. states and their capitals
    states_and_capitals = {
        "Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix", "Arkansas": "Little Rock",
        "California": "Sacramento", "Colorado": "Denver", "Connecticut": "Hartford", "Delaware": "Dover",
        "Florida": "Tallahassee", "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise",
        "Illinois": "Springfield", "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka",
        "Kentucky": "Frankfort", "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
        "Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
        "Missouri": "Jefferson City", "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
        "New Hampshire": "Concord", "New Jersey": "Trenton", "New Mexico": "Santa Fe", "New York": "Albany",
        "North Carolina": "Raleigh", "North Dakota": "Bismarck", "Ohio": "Columbus", "Oklahoma": "Oklahoma City",
        "Oregon": "Salem", "Pennsylvania": "Harrisburg", "Rhode Island": "Providence", "South Carolina": "Columbia",
        "South Dakota": "Pierre", "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City",
        "Vermont": "Montpelier", "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston",
        "Wisconsin": "Madison", "Wyoming": "Cheyenne"
    }
    score = 0
    print("\nWelcome to the States and Capitals Quiz!")
    print("You will be given 5 questions. Try to match states with their capitals or vice versa.\n")
    for _ in range(10):  # Ask 10 random questions
        if random.choice([True, False]):
            # Ask for the capital of a state
            state, capital = random.choice(list(states_and_capitals.items()))
            answer = input(f"What is the capital of {state}? ").strip().title()
            if answer == capital:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The capital of {state} is {capital}.")
        else:
            # Ask for the state corresponding to a capital
            state, capital = random.choice(list(states_and_capitals.items()))
            answer = input(f"{capital} is the capital of which state? ").strip().title()
            if answer == state:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! {capital} is the capital of {state}.")
    print(f"\nYour final score: {score}/10")
    if score == 5:
        print("Excellent! You know your states and capitals!")
    elif score >= 3:
        print("Good job! A little more practice and you'll master it.")
    else:
        print("Keep practicing! You'll get there.")
    
# Main Program
def main():
    name = login()
    while True:
        choice = game_menu()
        if choice == 1:
            hangman()
        elif choice == 2:
            tic_tac_toe()
        elif choice == 3:
            math_quiz()
        elif choice == 4:
            ocean_test()
        elif choice == 5:
            periodic_table_quiz()
        elif choice == 6:
            states_capitals_quiz()
        elif choice == 7:
            amendments_quiz()
        elif choice == 8:
            print(f"Goodbye, {name}!")
          
if __name__ == "__main__":
    main()
