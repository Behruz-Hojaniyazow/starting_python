def even(num):
  """a function that checks whether odd number or even number"""
  return num % 2 == 0
while True:
  try:
    son = float(input("Enter a number: "))
    break
  except ValueError:
    print("Please, enter only numbers")
if even(son):
  print(f"{son} is - even number")
else:
  print(f"{son} is - odd number ")