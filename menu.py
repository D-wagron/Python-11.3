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


def cyoa_play_again():
    cyoa_play_again = input("Play again (y/n)?").lower()
    while cyoa_play_again not in ("y", "n"):
        print("Invalid input. Try again.")
        cyoa_play_again = input("Play again (y/n)?").lower()
    if cyoa_play_again == "y":
        play_cyoa()
    else:
        input("Press enter to return to the menu: ")


def play_cyoa():
    """Play CYOA game."""
    clear_screen()
    global cyoa_score
    global cyoa_name
    cyoa_score = 0
    make_sure = input("Input 0 to return to the menu if you wish to return, else leave empty: ")
    if make_sure == "0":
        menu()
        return
    clear_screen()
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
    print("If you win or die, you keep your points")
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
    if first == "l": # Pathway 2
        clear_screen()
        cyoa_score += 1
        print("You find youself inside of ")
        print("It seems a little bit drafty.")
        print("Do you try investigate, or find a way out of the vicious cold?")
        print("'I' for investigation, 'L' look for a way ot of the cold")
        pathway_six = input("Enter input here: ").lower() # Third option
        while pathway_six not in ("i", "l"):
            print("Invalid input. Try again")
            pathway_six = input("Enter input here: ").lower()
        if pathway_six == "i":
            clear_screen()  
            cyoa_score += 1
            print("You come face to face with a gaping hole.")
            print("It might not be that far down to the bottom.")
            print("Do you look in, or try jump across?")
            print("'L' for look, 'J' for jump")
            death_pit = input("Enter input here: ").lower()
            while death_pit not in ("l", "j"):
                print("Invalid input. Try again")
                death_pit = input("Enter input here: ").lower()
            if death_pit == "l": # Pit Death
                clear_screen()
                cyoa_score += 1
                print("As you investigate the hole, a strong gust of wind blows you off balance.")
                print("The hole give you the cold embrace of death.")
                print("Perhaps in another life you would have jumped.")
                print(f"Final score: {cyoa_score}")
                cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
                cyoa_play_again()
            else:
                clear_screen()
                cyoa_score += 1
                print("You leap acorss the pit, 'thud' your body hits the cold stone floor.")
                print("Your hands scrabble around you, until you are able to pull yourself up.")
                print("It is a lot darker this side, but your eyes adjust.")
                print("You find yourself standing in front of rusted barred cells, weapons strewn on the floor.")
                print("Any bodies that were here, are now long gone.")
                input("Press enter to continue: ")
                play_cyoa_II()

        else: # pathway 3
            clear_screen()
            cyoa_score += 1
            print("After a bit of wandering, you notice a large wooden staircase in front of you.")
            print("A little sign notes: 'All that be changed, stay changed'")
            print("The staircase goes both up and down")
            print("'U' for up, 'D' for down")
            option_four = input("Enter input here: ").lower()
            while option_four not in ("u", "d"):
                print("Invalid input. Try again.")
                option_four = input("Enter input here: ").lower()
            if option_four == "u": # Pathway 7 Tower Death
                clear_screen()
                cyoa_score += 1
                print("You find yourself at the top of a tower.")
                print("A short moment after looking around, you hear a 'crack' behind you.")
                print("Do you turn around (y/n)?")
                turn_around_death = input("Enter input here: ").lower()
                while turn_around_death not in ("y", "n"):
                    print("Invalid input. Try again.")
                    turn_around_death = input("Enter input here: ").lower()
                if turn_around_death == "n":
                    print("Perhaps in another life you would have turned around.")
                    print("You died. Must have been the wind.")
                    print(f"Final score: {cyoa_score}")
                    cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
                    cyoa_play_again()
                else:
                    clear_screen()
                    print("As you turn around, a gust of wind at around 408 km/h blows you off the tower.")
                    print("'Unfortunatley we were unable to recover your memories after that.'")
                    print("'All we could see was a Ford Focus, no clue why.'")
                    print("You are then sedated, and fall into an infinite coma.")
                    print(f"Final score: {cyoa_score}")
                    cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
                    cyoa_play_again()
            else:
                clear_screen()
                cyoa_score += 1
                print("You descend the staicase, light turning to gloom.")
                print("Your eyes adjust after a moment, barred cages line the walls, weapons of guards lie on the ground.")
                print("Any bodies that were here, are now long gone.")
                print("You find yourself in the dungeon.")
                input("Press enter to continue: ")
                play_cyoa_II()
    else:
        clear_screen()  # Pathway 1
        cyoa_score += 1
        print("You venture to the right, behind the throne, and find youself in a barren treasury.")
        print("Dust is caked onto every surface, and the air is thick, like smog.")
        print("'cough' You don't have much time.")
        print("To your left is a door, bolted shut and to the right is a semi-rumbled brick wall.")
        print("You have enough breath to choose one option and run at them.")
        print("Do you run at the door, or wall?")
        print("'D' for door, 'W' for wall")
        pathway_five = input("Enter input here: ").lower()
        while pathway_five not in ("d", "w"):
            print("Invalid input. Try again.")
            pathway_five = input("Enter input here: ").lower()
        if pathway_five == "d":
            clear_screen()
            cyoa_score += 1
            print("You run shoulder first into the door and thankfully the hinges give way and snap.")
            print("You run through, before you collaps to the floor, catching your precious breath.")
            print("In front of you lies the rusted remains of the feared dungeon of Loter Castle.")
            print("No one knows why it was feared, but nobody survived their capture.")
            input("Press enter to continue: ")
            play_cyoa_II()
        else:
            clear_screen()
            cyoa_score += 1
            print("You run full force at the wall,")
            print("and for a beautiful fraction of a second you think you've escaped.")
            print("However realty hits, but not as hard as the impact.")
            print("You break a few of your ribs, and puncture your lungs.")
            print("'we were unable to recover anything more, test subject.'")
            print(f"Final score: {cyoa_score}")
            cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
            cyoa_play_again()


def play_cyoa_II():
    clear_screen()
    global cyoa_name
    global cyoa_score
    cyoa_score += 1
    print("On the floor is a torch, but with no way to light it, you leave it.")
    print("You wander through the decrepid tunnel, your hand following the mossy stone wall.")
    print("But moss can't grow in total darkness, and the dungeon is too far underground for that.")
    print("As if it was never there, the moss dissapeared.")
    input("Press enter to continue: ")
    clear_screen()
    print("The end of the hall splits off into two rooms.")
    print("The one on the left holds rows of weapons and a few suits of armour.")
    print("The one on the right beckons to you with a faint blue glow.")
    print("'L' for left, 'R' for right")
    pathway_eight = input("Enter input here: ").lower()
    while pathway_eight not in ("l", "r"):
        print("Invalid input. Try again.")
        pathway_eight = input("Enter input here: ").lower()
    if pathway_eight == "l":
        clear_screen()
        cyoa_score += 1
        print("Inside the armoury, spearsline the walls, and a singular suit stands proud.")
        print("Do you stop and inspect the armour, or keep moving on.")
        print("'I' for inspect, 'M' to move on")
        suit = input("Enter input here: ").lower()
        while suit not in ("i", "m"):
            print("Invalid input. Try again.")
            suit = input("Enter input here: ").lower()
        if suit == "i":
            print("You step closer to the armour, fail to notice the axe poised high.")
            print("A mouse pokes out the visor, captivating you.")
            print("The blade swings down, and ...")
            print("'That's it for you.'")
            print("'No more life.'")
            print("A different voice that time.")
            input("Press enter to continue: ")
            clear_screen()
            print(f"Final score: {cyoa_score}")
            cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
            cyoa_play_again()
        else: 
            clear_screen()
            cyoa_score += 1
            print("The same enticing blue lights the end of the corridor, and you find yourself staring.")
            print("All around you are glyphs that pulse in and out, like a starry heartbeat.")
            print("At the end of the room is a solid oak door, that looks almost surreal, but it fits right in.")
            print("You feel compelled to open the door.")
            print("Do you (y/n)?")
            final_door = input("Enter input here: ").lower()
            while final_door not in ("y", "n"):
                print("Invalid input. Try again.")
                final_door = input("Enter input here: ").lower()
            if final_door == "n":
                print("You don't know what lies beyond that door.")
                print("But, you know you can't turn back now.")
                print("You push on further, and out the door.")
                input("Press enter to continue: ")
                play_cyoa_III()
            else:
                print("The door creaks open...")
                input("Press enter to continue: ")
                play_cyoa_III()
    else:
        clear_screen()
        cyoa_score += 1
        print("As you enter through the arched doorway, a pulse of light eminates from the room.")
        print("In time with your heart?")
        print("Each glyph seemingly a complete thought, but somehow unfinished.")
        print("At the end of the room is a solid oak door, that looks almost surreal, but it fits right in.")
        print("You feel compelled to open the door.")
        print("Do you (y/n)?")
        final_door = input("Enter input here: ").lower()
        while final_door not in ("y", "n"):
            print("Invalid input. Try again.")
            final_door = input("Enter input here: ").lower()
        if final_door == "n":
            print("You don't know what lies beyond that door.")
            print("But, you know you can't turn back now.")
            print("You push on further, and out the door.")
            input("Press enter to continue: ")
            play_cyoa_III()
        else:
            print("The door creaks open...")
            input("Press enter to continue: ")
            play_cyoa_III()


def play_cyoa_III():
    clear_screen()
    global cyoa_name
    global cyoa_score
    print("There.")
    print("In the middle.")
    print("You'd made it.")
    print("The idol lay on a marble pedestal.")
    print("It isn't much of an idol is it?")
    print("It's a stale, but perfectly golden-brown ham sandwich.")
    print("Who would have guessed.")
    print("Not me that's for sure.")
    input("Press enter to continue: ")
    clear_screen()
    print("You feel a rumbling, and before you realise you're not hungry, you start sweating.")
    print("Molten rock spews from fountains across the room, filling the pit below you.")
    print("Should you try escape with the idol?")
    print("The walls look fairly climbable, and you still have time.")
    input("Press enter to continue: ")
    clear_screen()
    print("The lava looks suspiciously..")
    print("...")
    print("hungry?")
    print("Taunt lava (y/n)?")
    taunt = input("Enter input here: ").lower()
    while taunt not in ("y", "n"):
        print("Invalid input. Try again.")
        taunt = input("Enter input here: ").lower()
    if taunt == "y":
        clear_screen()
        print("You tease the lava by holding the idol above your head.")
        print("Idol is very much the wrong word to be using, but anyway.")
        print("A burble of lava erupts from underneath you, engulfing you and the idol in flames.")
        print("Before you feel any pain your vision cuts out and you hear: ")
        print("'\x1B[3mNearly\x1B[23m'")
        print("'Send them in again.'")
        print(f"Final score: {cyoa_score}")
        cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
        cyoa_play_again()
    else:
        print("You return the idol to the marble pilar.")
        print("Damn that thing is heavy.")
        print("You might have an opportunity to escape now.")
        print("You sprint towards the most climbable section of the wall, and try reach out...")
        input("Press enter to continue: ")
        clear_screen()
        print("An echo from below.")
        print("'War never satisfied me, only prologed my hunger.'")
        print("Thank you mortal.")
        input("Press enter to continue: ")
        clear_screen()
        print("You won!")
        print("But did you?")
        print("You may have survived, but you failed to retreive the idol.")
        print("You sit down in the rain wondering if yor choices were truly yours to make.")
        print("'Well done, test subject, you passed.'")
        print("Your eyes open wide, you look around before you are quickly sedated.")
        print("'\x1B[3mWas it you who really chose?\x1B[23m'") #italics work for terinal, no idea for anything else
        print("\n ")
        cyoa_score += 5 # winning bonus
        cyoa_players.append({"name": cyoa_name, "score": cyoa_score})
        print(f"Final score: {cyoa_score}")
        cyoa_play_again()


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

