def mark_grade(score):
  if score >= 90: return "A"
  elif score >= 80: return "B"
  elif score >= 70: return "C"
  elif score >= 60: return "D"
  else : return "E"

user = int(input ("What is your percentage?"))
grade = mark_grade(user);
print (grade)
