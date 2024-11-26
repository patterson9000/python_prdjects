import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    while True:
        guess = input("Guess (space-separated colors): ").upper().split()
        
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue
        
        if not all(color in COLORS for color in guess):
            print(f"Invalid color in guess. Valid colors are: {', '.join(COLORS)}.")
            continue

        return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1

   
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_counts[guess[i]] -= 1

    
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i] and color_counts.get(guess[i], 0) > 0:
            incorrect_pos += 1
            color_counts[guess[i]] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind! You have {TRIES} attempts to guess the code.")
    print("Valid colors are:", ", ".join(COLORS))
    
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"Congratulations! You guessed the code in {attempts} attempts.")
            break
        
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    
    else:
        print(f"Sorry, you've run out of tries. The code was: {' '.join(code)}")

if __name__ == "__main__":
    game()
