'''so is this
#This is a comment
#Flip a coin Program
from random import choice, random
#1st method use random.random()
#coin_flip_with_random = "Head" if random() > 0.5 else "Tails"
#2nd Method random.choice()
coin_flip_with_choice = choice(["Antarctica", "Area 51", "Mars", "The center of the Earth", "Ohio", "Santa's Workshop", "Alcatraz", "Heaven", "H E DoubLLe Hocky Sticks", "The Mariana Trench"])
print(coin_flip_with_choice)'''
#roll a dice
#1st report to your libraries
from random import randint
repeat = True
while repeat:
  print("You rolled", randint (1,6))
  print("You can try again")
  repeat = ("y or yes") in input().lower()
