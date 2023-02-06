# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:22:56 2023

@author: PCshop
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for char in range (1, nr_letters+1):
  password += random.choice(letters)
for char in range (1, nr_symbols+1):
  password += random.choice(symbols)
for char in range (1, nr_numbers+1):
  password += random.choice(numbers)

print(f"Your password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password1 = ""
password_list = []

for char1 in range (1, nr_letters+1):
  password_list.append(random.choice(letters))
for char1 in range (1, nr_symbols+1):
  password_list.append(random.choice(symbols))
for char1 in range (1, nr_numbers+1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
  password1 += char

print(f"Your password is: {password1}")