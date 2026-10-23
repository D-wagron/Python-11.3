import os

cyoa_players = []

cyoa_score = 0
cyoa_name = ""

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
    global cyoa_score
    global cyos_name
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
                # cyoa part 2

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
                #contine on with the dungeon part.
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
            # continue part 2 here:
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



play_cyoa()

# the puter has been diagnosed, unfortunatley it is terminal :]