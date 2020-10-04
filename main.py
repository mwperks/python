import random
x = random.randrange(1,10)
guess = int(input("Guess a number between 1 and 10"))
while guess != x:
  print ("Sorry, wrong answer, try again. \n")
  guess = int(input("Guess a number between 1 and 10: "))
print ("Congratulations!  You guessed correctly!")