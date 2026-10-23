import os

cyoa_players = []


def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
    lava_distance = 100
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
            third = input("Enter input here: ").lower()
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
                cyoa_play_again()

            else:
                clear_screen()
                cyoa_score += 1
                print("You leap acorss the pit, 'thud' your body hits the cold stone floor.")
                print("Your hands scrabble around you, until you are able to pull yourself up.")

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
            if option_four == "u": # Pathway 7
                clear_screen()
                cyoa_score += 1
                print("")
            else:
                clear_screen()
                cyoa_score += 1
                print("")





    
    else:
        clear_screen()  # Pathway 1
        cyoa_score += 1

play_cyoa()

# the puter has been diagnosed, unfortunatley it is terminal :]