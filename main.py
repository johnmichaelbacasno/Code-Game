from utils import unique_number, generate_result

def Code_Game(difficulty) -> None:
    """A function that plays the Code Game"""
    difficulty = 10 if difficulty > 10 else difficulty
    tries = 0
    secret_number = unique_number(difficulty)

    # Display instructions
    print("Welcome to Code, the Game!",
          f"The computer will make a secret combination made out of {difficulty} unique numbers from 0 to 9",
          "Your job is to figure out the combination with the help of clues",
          "\n(0) means that the digit is correct and in the correct position",
          "(X) means that the digit is correct but in the wrong position",
          "(-) means that the digit guessed is wrong\n",
          sep="\n"
          )
    
    while True:
        # Handles input errors
        try:
            user_number = input(f"Please input {difficulty} unique digits: ")
            # Input must be a number
            if not user_number.isnumeric(): raise ValueError("Input must be a number")
            # Input must be `difficulty` characters long
            if not len(user_number) == difficulty: raise ValueError(f"Input must be {difficulty} characters long")
        except:
            print("Try again\n")
            continue
        
        result = generate_result(user_number, secret_number)
        tries += 1
        
        print("YOUR INPUT" + ("| {} " * difficulty).format(*user_number))
        print("   RESULT "  + ("| {} " * difficulty).format(*result) + "\n")
        
        # Stop if the user has solved the game
        if user_number == secret_number: break
    
    # Display congratulations message
    print(f"Congratulations! You solved it in {tries} tries")