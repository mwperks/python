def menu():
    menuOption=int(input("Select an option 1,2 or 3"))
    if(menuOption==1):
      print("These are all the Running Trainers")
    elif(menuOption==2):
      print("these are all the Classics")
    elif(menuOption==3):
      print("This is all the Boots and Shoes")
    else:
      print("You didn't choose the correct option")

menu()