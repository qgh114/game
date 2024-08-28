from art import *
import time
from ascii_magic import AsciiArt

class Question:
    def __init__(self, questionText, answer):
        self.questionText = questionText
        self.answer = answer
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +'}'



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
Question("Which actor played Iron Man in the Marvel Cinematic Universe?", " Robert Downey Jr")
]


print("Answer my question and you might live")
for question in quizQuestions:
    print(f"{question.questionText}?")
    userInput = input()

    if (userInput.lower() == question.answer.lower()):
        print("That is correct!")
    else:
        tprint("Wrong! You Die!")
        my_art2.to_terminal()
        break;
