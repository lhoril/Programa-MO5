import random

def guessCharacter():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    character_to_guess = random.choice(characters)
    attempts = 0
    guessed = False
    
    print("Welcome to the Guess the Character game!")
    print("I've chosen a character from 'a' to 'z'. Can you guess it?")
    
    while not guessed:
        guess = input("Enter your guess: ").lower()
        attempts += 1
        
        if guess == character_to_guess:
            print(f"Congratulations! You guessed the character '{character_to_guess}' in {attempts} attempts!")
            guessed = True
        else:
            print("Incorrect guess. Try again.")

if __name__ == "__main__":
    guessCharacter()