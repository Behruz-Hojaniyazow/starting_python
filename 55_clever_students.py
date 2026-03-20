clever_students = 0
fallen = 0
i = 1
while i <= 5:
  try:
    score_input = input(f"How many points did student {i} get? ")
    score = float(score_input)
    if 0 <= score <= 100:
      if score >= 90:
        clever_students += 1
      else:
        fallen += 1
      i += 1
    else:
      print("please enter a score between 0 and 100")
  except ValueError:
    print("Error, please enter only numbers")
print("*" * 30)
print(f"{clever_students} student/s passed with a high point")
print(f"{fallen} student/s passed with a low point")