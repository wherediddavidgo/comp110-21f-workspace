"""A test to decide whether the player is more like Adin Zimmerman or David Go."""
__author__: str = "730407005"
__name__: str = "__main__"
points: int = 0
choice: int
NAMED_CONSTANT: str = "\U00000000"
def main() -> None:
    """main controls the flow of the game"""
    global points
    greet()
    game_loop: int = int(input("What would you like to do? 1 to play, 2 to quit "))
    i: int
    while game_loop == 1:
        i = 0
        
        while i < 3:
            questionGenerator()
            choice = int(input())
            scorer(choice)
            if points == 1:
                print(f"You have {points} point.")
            else:
                print(f"You have {points} points.")
            i += 1
        game_loop = int(input("You've played three rounds. Would you like to keep going? 1 to play, 2 to quit "))
        while game_loop != 1 and game_loop != 2:
            game_loop = int(input("That's not a valid choice. Please select again. 1 to play, 2 to quit "))
    #quit

def greet() -> None:
    """gets player's name so it can be included in computer interaction with player"""
    print("Are you more David Go or Adin Zimmerman?")
    global player
    player = input("What is your name? ")

def scorer(choice: int) -> int:
    """checks whether answer is more David-like or Adin-like and adds or subtracts points accordingly"""
    global points
    if choice == 2:
        points += 1
        print(f"{player}, you've earned a point for being more like David! Good job \U0001F973")
    elif choice == 1:
        points -= 1
        print(f"{player}, you've lost a point for being more like Adin! Better luck next time \U0001F62D")
    else:
        print("That's not a valid choice. Try again. \U0001F615")
    return(points)

def questionGenerator() -> None:
    """randomly selects a question from a list"""
    from random import randint
    question: str = ""
    rng: int = randint(1, 7)
    if rng == 1:
        print("Are you allergic to nuts? \U0001F95C 1 for Yes, 2 for No")
    elif rng == 2:
        print("Do you have curly hair? 1 for Yes, 2 for No")
    elif rng == 3:
        print("Is your height >= 5 feet 9 inches? \U00002B06\U00002B07 1 for Yes, 2 for No")
    elif rng == 4:
        print(f"What's your major? 1 for computer science \U0001F4BB, 2 for geology \U000026F0")
    elif rng == 5:
        print("What is your favorite sport? 1 for hockey \U0001F3D2, 2 for track and field \U0001F3BD")
    elif rng == 6:
        print("Is your dorm decorated nicely? 1 for yes, 2 for no")
    elif rng == 7:
        print("Which mRNA vaccine did you get? \U0001F489 1 for Moderna, 2 for Pfizer")

if __name__ == "__main__":
    main()