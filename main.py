def mark_grade(score):
  if score >= 90: return "A"
  elif score >= 80: return "B"
  elif score >= 70: return "C"
  elif score >= 60: return "D"
  else : return "E"

user = int(input ("What is your percentage?"))
Target = input ("What is your target grade?")
grade = mark_grade(user);
print ("Your target is " + Target + " and your grade is" + grade )
if grade < Target:
    print ("You have not passed")
elif grade == Target:
    print ("You have achieved your pass mark")
elif grade > Target:
    print ("You have passed with honours!")
else:
    print ("Need to study more")