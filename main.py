palindrome = input("Please enter a word you think is a palindrome:")

palindrome2 = palindrome[::-1]

if palindrome == palindrome2:
  print ("Correct that is a palindrome!")
else:
  print("Sorry, try again!")