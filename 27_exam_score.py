students_scores = {}
while True:
  print("Type 'Stop' to stop the project")
  student = input("Enter the student's name ").title()
  if student == 'Stop':
    print("project was stopped")
    break
  else:
    while True:
      try:
        score = float(input(f"enter {student}'s score: "))
  
        students_scores[student] = score
        break
      except ValueError:
        print("Please enter only numbers, Try again")
if students_scores:
  all_scores = list(students_scores.values())
  highest_score = max(all_scores)
  lowest_score = min(all_scores)
  average_score = sum(all_scores) / len(all_scores)
  for student, score in students_scores.items():
   print(f"{student} got {score} scores")
print(f"The highest score in class is {highest_score}")
print(f"The lowest score in class is {lowest_score}")
print(f"Average score in class is {average_score}")
else:
  print("Still no one has taken exam")