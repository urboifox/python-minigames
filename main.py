import sys, random, math, os

from helpers.hangman import display_hangman, get_word
from helpers.wordle import get_wordle

class GameMessage:
    INVALID_GAME_NUMBER = f"Please enter a valid game number"
    INVALID_NUMBER = f"Oops, that wasn't really a number"

    @classmethod
    def BREAK(cls, n = 50):
        return "=" * n

class Player:
    score = 0

    @classmethod
    def set_score(cls, score: int):
        if score < 0:
            raise ValueError("Invalid score")
        cls.score = score
    
    @classmethod
    def increment_score(cls, points: int) -> None:
        cls.score += points

def main():
    game_loop()

def print_game_menu():
    print("1. Hangman")
    print("2. Worlde")
    print("3. Guess the number")
    print("0. Exit")

def game_loop() -> None:
    valid_input_numbers = (1,2,3,0)
    while True:
        print_game_menu()
        try:
            game_number = int(input("Pick a game: ").strip())
        except KeyboardInterrupt:
            exit_game()
        except ValueError:
            message(GameMessage.INVALID_GAME_NUMBER)
            continue
        else:
            if game_number not in valid_input_numbers:
                message(GameMessage.INVALID_GAME_NUMBER)
                continue


        if game_number == 1:
            hangman()
        elif game_number == 2:
            wordle()
        elif game_number == 3:
            guess_game()
        elif game_number == 0:
            exit_game()

def wordle():
    word = get_wordle()
    attempts = 6
    guessed_words = []

    def colored_text(text, color):
        colors = {
            "green": "\033[92m",
            "yellow": "\033[93m",
            "reset": "\033[0m"
        }
        return f"{colors[color]}{text}{colors['reset']}"

    clear_screen()
    message("Welcome to Wordle! Guess the 5-letter word.")

    while attempts > 0:
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Enter your guess: ").strip().lower()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        
        guessed_words.append(guess)
        clear_screen()
        
        if guess == word:
            print(f"\nYou guessed it! The word was [ {word} ]")
            print(f"Number of attempts: {6 - attempts}")
            Player.increment_score(int(6 / attempts))
            print_score()
            return
        
        for gw in guessed_words:
            feedback = ""
            for i in range(5):
                if gw[i] == word[i]:
                    feedback += colored_text(gw[i].upper(), "green")  # Correct letter in the correct place
                elif gw[i] in word:
                    feedback += colored_text(gw[i], "yellow")  # Correct letter in the wrong place
                else:
                    feedback += gw[i]  # Incorrect letter
            print(feedback)
        
        attempts -= 1
    
    message(f"\nYou didn't get it right this time, the word was [ {word} ]")
    print_score()


def hangman():
    attempts = 6
    word = get_word()
    guessed_letters = set()

    while attempts >= 0:
        clear_screen()
        message(f"Welcome to Hangman! The word has {len(word)} letters.")
        all_letters_guessed = True
        # Check if all letters are guessed
        for l in word:
            if l not in guessed_letters:
                all_letters_guessed = False
                break
        
        if all_letters_guessed:
            print(f"\nYou guessed it! the word was [ {word} ]")
            print(f"Number of attempts: {6 - attempts}")
            print_score()
            return

        display_hangman(attempts)
        print(f"Remaining attemps: {attempts + 1}")

        print("Guessed letters: [", end="")
        for l in sorted(guessed_letters):
            print(f" {l} ", end="")
        print("]\n")

        for l in word:
            if l in guessed_letters:
                print(f" {l} ", end="")
            else:
                print(" _ ", end="")
        print("\n")
        
        while True:
            try:
                guess = input("Guess a letter: ").strip()
            except KeyboardInterrupt:
                exit_game()
            if len(guess) != 1:
                print("Enter one letter!")
            else:
                break
        
        if guess not in word and guess not in guessed_letters:
            attempts -= 1
        guessed_letters.add(guess)

    message(f"\nYou didn't get it right this time, the word was [ {word} ]")
    print_score()
        




def guess_game():
    clear_screen()
    message("Welcome to Guess the Number!")
    while True:
        try:
            level = int(input("Level: ").strip())
        except KeyboardInterrupt:
            exit_game()
        except ValueError:
            print(GameMessage.INVALID_NUMBER)
            pass
        else:
            if level < 1 or level > 10:
                print("Enter a number between 1 - 10")
            else:
                break
    clear_screen()
    level_range = int(math.pow(10, level))
    target = random.choice(range(1, level_range))
    attempts = 0

    message(f"Pick a number from 1 - {level_range} or type '0' to exit.")

    while True:
        try:
            number = int(input("Guess: ").strip())
            number = int(number)
        except KeyboardInterrupt:
            exit_game()
        except ValueError:
            message(GameMessage.INVALID_NUMBER)
            continue

        attempts += 1
        if number == 0:
            return
        if number == target:
            if attempts <= 10:
                Player.increment_score(int(10 / attempts))
            print(f"\nYou guessed it! the number was {target}")
            print(f"Number of attempts: {attempts}")
            print_score()
            break
        elif number >= target:
            print(random.choice(["Too high!", "Lower!", "That's not it!"]))
        else:
            print(random.choice(["Too low!", "Higher!", "That's not it!"]))

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def print_score() -> None:
    print(f"\nTotal score is [ {Player.score} ]\n")

def exit_game() -> None:
    message(f"Total score is [ {Player.score} ]")
    sys.exit(f"Thanks for playing!")

def message(m):
    print(f"\n", GameMessage.BREAK(len(m)), sep="")
    print(m)
    print(GameMessage.BREAK(len(m)), f"\n")


if __name__ == "__main__":
    main()