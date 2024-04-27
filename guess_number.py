import random
random_number = random.randint(1,10)
guess = int(input("ENTER THE NUMBER: "))
while(guess != random_number):
  print("try again")
  guess = int(input("ENTER THE NUMBER: "))
print("RIGHT GUESS!!!!")