username=input("ENTER A USERNAME FOR THIS GAME: ")


import random
import os

secretnum=random.randint(1,50)
score=0
while True: 
   os.system('cls' if os.name == 'nt' else 'clear')
   guess=int(input("Guess a number between {1-50}: "))
   score+=5
   if guess==secretnum:
      print(f"{username}You guessed it!")
      print(f"{username} your score:", score)
      print(f"{username} YOU GUESSED IT IN {score} ROUNDS.")
   playagain=input('enter yes to continue or no to quit: ')
   if playagain=="yes":
    secretnum=random.randint(1,50)
    score=0
   else : 
    break