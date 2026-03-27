def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers")
def add_students():
  """a function that collectes students into a dictionary"""
  students = {}
  while True:
    name = input("Enter the student's name: ").title()
    score = get_number(f"Enter {name}'s score: ")
    students[name] = score
    stop = input("Do you want to add one more student? (yes/no)").lower()
    if stop == 'no':
      break
  return students
def calculate_average(students):
  """a function that calculates the average score of students"""
  if not students:
    return 0
  return sum(students.values()) / len(students)
  return average
def find_best_student(students):
  """ a function that finds the best student in the dictionary"""
  if not students:
    return None
  return max(students, key=students.get)
def display_results(students, average, best_student):
  """ a function that displays all results"""
  print("\n" + "=" * 30)
  print("        STUDENTS LIST")
  print("=" * 30)
  for name, score in students.items():
    print(f"\nUser: {name} | Score: {score}")
  print("-" * 30)
  print(f"Average score: {average:.2f}")
  print(f"The best student: {best_student}")
  print("=" * 30)
#-----STARTING THE PROGRAM (ENGINE PART)----
if __name__ == "__main__":
  #Collecting the informations
  my_class = add_students()
  #calculating scores
  avg_score = calculate_average(my_class)
  top_student = find_best_student(my_class)
  display_results(my_class, avg_score, top_student)