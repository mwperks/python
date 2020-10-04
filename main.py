def shoePrice

if (shoePrice < 9.99):
  cheapShoe=True
else:
  cheapShoe=False
if (not(cheapShoe)):
  print("The shoe is expensive")
else:
  print("This shoe is cheap")