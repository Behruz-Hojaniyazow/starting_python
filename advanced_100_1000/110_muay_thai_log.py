def daily_exercises():
  """function that saves the daily exercises to the new file"""
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}! Enter your daily exercises---\n")
  exercises = []
  print("Type (stop) to finish")
  while True:
    exercise = input("Enter the exercise: ").strip()
    if exercise.lower() == 'stop':
      break
    exercises.append(exercise)
  if exercises:
    filename = 'muay_training.txt'
    with open(filename, 'a', encoding = 'utf-8') as file:
      for exercise in exercises:
        file.write(f"{exercise.lower()}\n")
    if len(exercises) > 1:
      print(f"{len(exercises)} exercises were saved successfully to the file '{filename}'")
    else:
      print(f"{len(exercises)} exercise was saved successfully to the file '{filename}' ")
  else:
    print("No exercises entered, File was not created")
if __name__ == '__main__':
  daily_exercises()