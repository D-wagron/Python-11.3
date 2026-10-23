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
    print("The one on the left holds rows of weapons and s few suits of armour.")
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
            print("'That's it for now.'")
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
            final_door = input("Enter input here: ")
            while final_door not in ("y", "n"):
                print("Invalid input. Try again.")
                final_door = input("Enter input here: ")
            if input == "n":
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
        final_door = input("Enter input here: ")
        while final_door not in ("y", "n"):
            print("Invalid input. Try again.")
            final_door = input("Enter input here: ")
        if input == "n":
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

    #normal ending
    # print("'\x1B[3mNearly\x1B[23m'")
    # print("'Send them in again.'")

    # true ending
    # print("You won!")
    # print("But did you?")
    # print("You may have survived, but you failed to retreive the idol.")
    # print("You sit down in the rain wondering if yor choices were truly yours to make.")
    # print("'Well done, test subject, you passed.'")
    # print("Your eyes open wide, you look around before you are quickly sedated."
    # print("'\x1B[3mWas it you who really chose?\x1B[23m'") #italics work for terinal, no idea for anything else


play_cyoa_II()

# the puter has been diagnosed, unfortunatley it is terminal :