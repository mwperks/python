
number=int(input("Enter a number between 1 and 10! "))
if (number==5):
  print("CORRECT!! Your a genius!")
else:
  print("Try again!")
total = 0
for i in range(100):
    for n in range(1,6):
        generatedNum = 0
        while generatedNum != n:
            #generate random number
            total += 1
print (total/100)