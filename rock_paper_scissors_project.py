# -*- coding: utf-8 -*-
"""Rock Paper Scissors Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JaFlFcAgJfpyQS9pJZvJ2C5AEyckcivB

An AI driven Rock Paper Scissors game.

The first choice is the User's to make, via an input function.

We then capitalize their choice to ensure the input string matches the string options in the logic.

A first IF statement checks to see if the input is valid. 

If the input is valid then the next IF statement checks to see if there is a tie. 

If there isn't then the remaining ELIF statements check the inputs to define an outcome and a winner.
"""

import random
choice = input("Enter your choice: Rock, Paper, or Scissors?? ")
user = choice.capitalize()
if user != "Rock" and user !="Paper" and user !="Scissors":
  print("invalid input. Please choose Rock, Paper, or Scissors and capitilize the word if you didn't already.")
elif user == "Rock" or "Paper" or "Scissors":
  choices = ["Rock","Paper","Scissors"]
  ai = random.choice(choices)
  print("Your pick is "+ user + ". " + "The Computer picks " + ai + ".")
  if user == ai:
    print("It's a draw...")
  elif user == "Rock" and ai == "Scissors":
    print("Rock smashes Scissors, you win!")
  elif user == "Rock" and ai == "Paper":
    print("Paper covers Rock, you lose :(")
  elif user == "Paper" and ai == "Rock":
    print("Paper covers Rock, you win!")
  elif user == "Paper" and ai == "Scissors":
    print("Scissors cut Paper, you lose :(")
  elif user == "Scissors" and ai == "Paper":
    print("Scissors cut Paper, you win!")
  elif user == "Scissors" and ai == "Rock":
    print("Rock smashes Scissors, you lose :(")