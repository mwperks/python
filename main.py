
import random
number_of_goes = 1
x = random.randrange(1,10)
print (x)
guess = int(input("Guess a number between 1 and 10"))
while guess != x and number_of_goes < 6:
  number_of_goes=number_of_goes + 1
  if (guess < x): 
    print ("Too low, try again! ")
  if (guess > x):
    print ("Too high, try again! ")
  
  guess = int(input("Guess a number between 1 and 10: "))
if (guess == x):
  print ("Congratulations!  You guessed correctly!")
else:
  print ("Sorry you have used all your guesses!")