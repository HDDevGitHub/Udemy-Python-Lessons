# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 12:24:16 2023

@author: PCshop
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
20
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
your_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors  ===>  "))
game_images = [rock, paper, scissors]
if your_choise>=3 or your_choise<0:
  print("You type an invalid number, You lose!")
else:  
  print(f"Your Choise is {game_images[your_choise]}")
  comp_choise = random.randint(0,2)
  print (f"Computer Choise is {game_images[comp_choise]}")

  if (your_choise==0) and (comp_choise==1): 
    print("You Lose!")
  elif (your_choise==0) and (comp_choise==2): 
    print("You Win!")
  elif (your_choise==1) and (comp_choise==0): 
    print("You Win!")
  elif your_choise==1 and comp_choise==2: 
    print("You Lose!")
  elif your_choise==2 and comp_choise==0: 
    print("You Lose!")
  elif your_choise==2 and comp_choise==1: 
    print("You Win!")
  else:
    print("Draw!")