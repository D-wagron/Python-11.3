"""Digitech asessment."""

import os
import random

roulette_players = []
number_players = []
cyoa_players = []


def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def play_roulette():
    """Play roulette game."""
    wins = 0
    roulette_name = ""
    roulette_difficulties = {
        "1": ("Easy", 8),
        "2": ("Normal", 6),
        "3": ("Hard", 4),
        "4": ("Quit", 0)
    }
    print("Welcome to a less dangerous version of Russian roulette")
    print("\nSelect difficulty:")
    for key, (name, chambers) in roulette_difficulties.items():
        print(f"{key}. {name} ({chambers} chambers)")
    print("\nSurvival rates:")
    print("Easy: High")
    print("Normal: Enough")
    print("Hard: Low")
    print("\nChoose difficulty (1-4):")
    print("Or enter 4 to quit")
    difficulty = input("\nEnter input here: ")
    while difficulty not in roulette_difficulties:
        difficulty = input("Invalid choice. Choose difficulty (1-4): ")
    if difficulty == "4":
        input("Press enter to return to the menu: ")
        menu()
        return
    difficulty_name, chamber_count = roulette_difficulties[difficulty]
    print(f"\nDifficulty set to {difficulty_name}!")
    print("Welcome to a less dangerous version of Russian roulette")
    roulette_name = input("Please enter your name: ")
    while True:
        clear_screen()
        input("Press enter to play...")
        chamber = random.randint(1, chamber_count)
        if chamber == 1:
            print("You died.")
            print(f"Final Score: {wins}")
            roulette_players.append({"name": roulette_name, "score": wins, "difficulty": difficulty_name})
            input("Press enter to return to the menu. ")
            break
        else:
            wins += 1
            print(f"You survived! Round(s) won: {wins}")
            roulette_again = input("Play again? (y/n): ").lower()
            while roulette_again not in ("y", "n"):
                roulette_again = input("Invalid input. Play again? (y/n): ").lower()
            if roulette_again == "n":
                print(f"Your final score was: {wins}")
                roulette_players.append({"name": roulette_name, "score": wins, "difficulty": difficulty_name})
                input("Press enter to return to the menu. ")
                break


def play_number(): 
    """Play number game."""
    guessed = []
    number_difficulties = {
        "1": ("Easy", 5),
        "2": ("Normal", 10),
        "3": ("Quit", 0),
    }
    print("Welcome to a number guessing game!")
    print("Select difficulty: ")
    for keys, (name, nambers) in number_difficulties.items():
        print(f"{keys}. {name} ({nambers} total numbers)")
    print("\nChoose difficulty (1-3)")
    print("Or enter 3 to return to the menu.")
    number_difficulty = input("\nEnter input here: ")
    while number_difficulty not in number_difficulties:
        number_difficulty = input("Invalid choice. Choose difficulty (1-3): ")
    if number_difficulty == "3":
        input("Press enter to return to the menu: ")
        menu()
        return
    number_difficulty_name, total_numbers = number_difficulties[number_difficulty]
    print(f"\nDifficulty set to {number_difficulty_name}!")
    input("Press enter to continue: ")
    clear_screen()
    print(f"Try to guess my number between 1 and {total_numbers}.")
    print("You have three guesses.")
    print("At the end of the round your score will be increase by 1 if you guess correctly.")
    input("Press enter to continue. ")
    clear_screen()
    guesses = 0
    number = random.randint(1, total_numbers)
    number_name = input("Please enter your name: ")
    current_wins = 0
    while True:
        clear_screen()
        print(f"Guess my number from 1-{total_numbers}")
        if guessed:
            print("Guessed numbers:")
            for numbers in guessed:
                print(numbers)
        if guesses >= 3:
            print(f"Game over! You ran out of guesses. The number was {number}.")
            print(f"Final score: {current_wins}")
            print("Your guesses:")
            for numbers in guessed:
                print(numbers)
            number_players.append({"name": number_name, "score": current_wins, "difficulty": number_difficulty_name})
            guessed = []
            current_wins = 0
            number_again = input("Play again? (y/n): ").lower()
            while number_again not in ("y", "n"):
                number_again = input("Invalid input. Play again (y/n): ").lower()
            if number_again == "y":
                clear_screen()
                guessed = []
                guesses = 0
                number = random.randint(1, total_numbers)
            else:
                break
        print(f"Guesses used: {guesses}/3")
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess < 1 or guess > total_numbers:
                print(f"Please guess a number between 1 and {total_numbers}.")
                input("Press enter to continue. ")
                continue
            if guess in guessed:
                print("Number already guessed.")
                input("Press enter to continue: ")
                continue
            guessed.append(guess)
            guesses += 1
        except ValueError:
            print("Invalid input! Please enter a number.")
            input("Press enter to continue. ")
            continue
        if guess == number:
            print("Correct!")
            print(f"The number was {number}")
            current_wins += 1
            print(f"Win streak {current_wins}")
            number_again = input("Play again? (y/n): ").lower()
            while number_again not in ("y", "n"):
                number_again = input("Invalid input. Play again (y/n): ").lower()
            if number_again == "y":
                clear_screen()
                guessed = []
                guesses = 0
                number = random.randint(1, total_numbers)
            else:
                input("Press enter to return to the menu.")
                print(f"Final score: {current_wins}")
                number_players.append({"name": number_name, "score": current_wins, "difficulty": number_difficulty_name})
                current_wins = 0
                guessed = []
                break
        else:
            print("Try again!")
            input("Press enter to continue. ")


def play_cyoa():
    """Play CYOA game."""
    cyoa_score = 0
    cyoa_name = input("Please enter your name: ")
    clear_screen()
    print("You have been tasked with recovering the golden idol.")
    print("The idol was last seen in Lobter Castle.")
    print("However much of the castle was destroyed from the Hampter siege.")
    print("Do what you can to bring the idol back into possession of Lord Honse.")
    print("Even if it costs your life.")
    input("Press enter to continue: ")
    clear_screen()
    print("You will recieve a point for every room you progress through.")
    print("If You die, your points will be lost.")
    print("If you win, you keep your points")
    input("Press enter to continue: ")
    clear_screen()
    print("You stare into down the to the end of what used to be a grand hall.")
    print("Crumbling stone arches and half torn tapestries lines the walls.")
    print("You reach the end of the hall. Do you go left or right?")
    print("'L' for left, 'R' for right.")
    first = input("Enter input here: ").lower()
    while first not in ("l", "r"):
        print("Invalid input. Try again")
        first = input("Enter input here: ").lower()
    if first == "l":
        clear_screen()  # Option 1
        cyoa_score += 1
        print("As you enter through the oak door, the hinges jam behind you.")
        input("Press enter to continue: ")
        print("Dust floats down from the ceiling in thick blankets.")
        print("You suffocate to death.")
        print(f"Name: {cyoa_name} Score: {cyoa_score}")
        cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
        input("Press enter to return to the menu: ")
    else:
        clear_screen()  # Option 2
        cyoa_score += 1
        print("Right")
        print("You climb through the hole in the wall, and sit outside enjoying the sunlight.")
        input("Press enter to continue: ")
        print("You were sitting there so long you died of starvation.")
        print(f"Name: {cyoa_name} Score: {cyoa_score}")
        cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
        input("Press enter to return to the menu: ")


def all_scores():
    """Highscore function"""
    clear_screen()
    if not roulette_players and not number_players and not cyoa_players:
        print("No scores recorded yet.")
        input("Press enter to return to the menu: ")
    else:
        if roulette_players:
            print("\n======== Roulette High Scores: ========")
            sorted_roulette = sorted(roulette_players, key=lambda x: x["score"], reverse=True)
            for name in sorted_roulette:
                print(f"Name: {name['name']} - Score: {name['score']} - Difficulty: {name['difficulty']}")
        if not roulette_players:
            print("No recorded scores yet for Roulette, go play!")
        if number_players:
            print("\n===== Number Guesser High Scores: =====")
            sorted_number = sorted(number_players, key=lambda x: x["score"], reverse=True)
            for name in sorted_number:
                print(f"Name: {name['name']} - Score: {name['score']} - Difficulty: {name['difficulty']}")
        if not number_players:
            print("\nNo recorded scores yet for Number Guesser, go play!")
        if cyoa_players:
            print("\n== Choose Your Own Adventure Scores: ==")
            sorted_cyoa = sorted(cyoa_players, key=lambda x: x["score"], reverse=True)
            for name in sorted_cyoa:
                print(f"Name: {name['name']} - Score: {name['score']}")
        if not cyoa_players:
            print("\nNo recorded scores yet for Choose Your Own Adventure, go play!")
        print("\n")
        input("Press enter to return to the menu: ")


def menu():
    while True:
        try:
            clear_screen()
            print("-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("          Games          ")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("1. Russian Roulette")
            print("2. Number Game")
            print("3. Choose Your Own Adventure")
            print("4. High Scores")
            print("5. Exit")
            start = int(input("\nEnter your choice (1-5): "))
            if start == 1:
                clear_screen()
                play_roulette()
            elif start == 2:
                clear_screen()
                play_number()
            elif start == 3:
                clear_screen()
                play_cyoa()
            elif start == 4:
                all_scores()
            elif start == 5:
                break
            elif start < 1 or start > 5:
                input("Please enter a number 1-5. Press enter to try again.")
            else:
                input("Invalid choice. Press enter to try again. ")
        except ValueError:
            input("Invalid input. Please only enter a number. Press enter to continue. ")


menu()


# the puter has been dignosed, unfortunatley it is terminal :]

#     if number_difficulty == "3":
#         menu()
#         return

