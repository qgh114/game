from art import *
import time
import random
from ascii_magic import AsciiArt

class Question:
    def __init__(self, questionText, answer):
        self.questionText = questionText
        self.answer = answer
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'


    def guessNumberGame(self):
        tprint("I'm thinking  of  a  number")
        time.sleep(3)
        tprint("between 1 and 15")

        time.sleep(3)
        tprint("Guess right and you may live")

        time.sleep(3)
        tprint("Guess wrong and you die")

        secret_number = random.randint(1, 15)
        attempts = 3

        print(f"You have {attempts} attempts to guess the correct number")

        for attempt in range(1, attempts + 1):
            guess = int(input(f"Attempt {attempt}: Make a guess: "))

            if guess == secret_number:
                print("Congratulations! You guessed the correct number!")
                break
            elif guess < secret_number:
                print("Too low.")
            else:
                print("Too high.")

            if attempt == attempts:
                    tprint("Wrong! You Die!")
                    my_art2.to_terminal()
            else:
                print(f"You have {attempts - attempt} attempts left. Try again")

my_art = AsciiArt.from_image('jigsaw.jpg')
my_art2 = AsciiArt.from_image('gun.jpg')

tprint("Hello there Academist!")
time.sleep(2)
tprint("You dont know me")
time.sleep(1)
tprint("But i know about you!")
time.sleep(2)
my_art.to_terminal()
tprint("I Want To Play A Game")


quizQuestions = [
Question("In what country were the first potatoes fried and served as French fries?", "Belgium"),
Question("Which band wrote the famous song Stairway to Heaven?", "Led Zeppelin"),
Question("Which football team is the best in the world", "Chelsea"),
Question("What is the smallest planet in our solar system?", "Mercury"),
Question("Which actor played Iron Man in the Marvel Cinematic Universe?", "Robert Downey Jr")
]

random.shuffle(quizQuestions)

print("Answer my question and you might live")
for question in quizQuestions:
    print(f"{question.questionText}?")
    userInput = input()

    if (userInput.lower() == question.answer.lower()):
        tprint("Correct! Lets play again shall we")
        time.sleep(2)
        question.guessNumberGame()
        break
    else:
        tprint("Wrong! You Die!")
        my_art2.to_terminal()
        break


