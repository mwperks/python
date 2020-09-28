import random
num_1=int(input("Enter your first number: "))

num_2=int(input("Enter your second number: "))

choice=str(input("Enter a if you want to add and b if you want to subtract "))
if choice=="a":
  print (int(num_1+num_2))
if choice=="b":
  print(int(num_1-num_2))