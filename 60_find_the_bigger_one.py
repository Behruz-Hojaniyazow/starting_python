def find_bigger():
  """a function that finds the bigger number"""
  while True:
    try:
      num1 = float(input("Enter the 1st number: "))
      break
    except ValueError:
      print("Please write only numbers, Try again")
  while True:
    try:
      num2 = float(input("Enter the 2nd number: "))
      break
    except ValueError:
      print("Please write only numbers, Try again")
  if num1 > num2:
    print(f"{num1} is bigger than {num2}")
  elif num2 > num1:
    print(f"{num2} is bigger than {num1}")
  else:
    print(f"{num1} and {num2} is equal")
find_bigger()