import random
import winsound
import time
import re
import os

#Program of Arnau, Works Good!
#This program tries to guess a random character.
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
            
##Oriol's Program
def telegraph():
    print("Enter a morse code message and the computer will play it:")
    correct = False
    message = input()
    while(not correct):
        correct =bool(re.match('^[\.\-\ *]+$',message))
        if(not correct):
            print("Morse code only uses .- or blank space please, try again:")
            print("If you want to quit enter E to exit:")
            message = input()
            if(message.upper=="E"):
                exit()
    for char in message:
        beep(char)

def beep(char):
    if(char=='.'):
        frequency = 600  
        duration = 100  
        winsound.Beep(frequency, duration)
    elif(char==' '):
        time.sleep(0.3)
    elif(char == '-'):
        frequency = 600 
        duration = 300  
        winsound.Beep(frequency, duration)

##Cristopher's Program
##This is a program that can make calculations.
def Calculator():
    total = 0
    TeclaFinal = ""
    while(TeclaFinal != "E"):
        try:
            number1 = int (input("Enter a number: "))
            os.system("cls")
            print("Select one operator to do the calculation")
            operator = input(f"{number1} ")
            os.system("cls")
            if(operator != 'X' and operator != '*' and operator != 'x' and operator != '+' and operator != '/' and operator != '-'):
                raise Exception("Introduce a correct operator")
            print("Enter the second number")
            number2 = int(input(f"{number1} {operator} "))
            os.system("cls")
            if(operator == 'X' or operator == '*' or operator == 'x'):
                total = number1 * number2
                print (f"{number1} {operator} {number2} = {total}")
            elif(operator == '+'):
                total = number1 + number2
                print (f"{number1} {operator} {number2} = {total}")
            elif(operator == '/'):
                total = number1 / number2
                print (f"{number1} {operator} {number2} = {total}")
            elif(operator == '-'):
                total = number1 - number2
                print (f"{number1} {operator} {number2} = {total}")
        except Exception as e:
            print(e)   
        TeclaFinal = input("if you want to continue using de calculator press INTRO and if you want to close it input E ")
        os.system("cls")

##MAIN
##The Main menu for the access from the programs.
if __name__ == "__main__":
    print("Choose a program to run")
    print("1-Guess the letter")
    print("2-Telegraph")
    print("3-Calculator")
    enter = input()
    while enter != "1" and enter != "2" and enter != "3":
        print("Wrong input try again")
        print("If you want to quit enter E to exit:")
        enter = input()
        if(enter.upper=="E"):
            exit()
    if enter.strip()=="1":
        os.system("cls")
        guessCharacter()
    if enter.strip()=="2":
        os.system("cls")
        telegraph()
    if enter.strip()=="3":
        os.system("cls")
        Calculator()
