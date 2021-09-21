__name__: str = "__main__"
score: int = 0
def main() -> None:
    greet()
    game_loop: int = int(input("What would you like to do? 1 to play, 2 to quit "))
    if game_loop == 1:
        print(f"You have {score} points.")
        choice = int(input(questionGenerator()))
        scorer(choice)
    


def greet() -> None:
    print("Are you more David Go or Adin Zimmerman?")
    global player
    player = input("What is your name? ")
choice: int


def scorer(choice: int) -> int:
    if choice == 2:
        score += 1
        print(f"{player}, you've earned a point for being more like David! Good job")
    elif choice == 1:
        score -= 1
        print(f"{player}, you've lost a point for being more like Adin! Better luck next time")
    else:
        print("That's not a valid choice. Try again.")
    return(score)

def questionGenerator() -> str:
    from random import randint
    question: str = ""
    rng: int = randint(1, 5)
    if rng == 1:
        question = "Are you allergic to nuts? 1 for Yes, 2 for No "
    elif rng == 2:
        question = "Do you have curly hair? 1 for Yes, 2 for No "
    elif rng == 3:
        question = "Is your height >= 5 feet 9 inches? 1 for Yes, 2 for No "
    elif rng == 4:
        question = "What's your major? 1 for computer science, 2 for geology "
    elif rng == 5:
        question = "What sports do you like? 1 for hockey, 2 for track and field "
    return(question)
"""
def gameControl() -> None:
    global choice
    choice = int(input("Enter your choice: "))
    print("What would you like to do? 1 to play, 2 to quit")
    if choice == 1:
        print(questionGenerator)
        scorer
"""
if __name__ == "__main__":
    main()