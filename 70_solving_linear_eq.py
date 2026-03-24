def get_number(prompt):
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers")
def linear_eq():
  """solving a linear equation in the form ax + b = 0"""
  print("We solve the equation ax + b = 0")
  a = get_number("Please enter the 'a': ")
  b = get_number("Please enter the 'b': ")
  if a == 0:
    if b == 0:
      print("The equation has infinite, many solutions.")
    else:
      print("The equation has no solution")
  else:
    x = -b / a
  print(f"Solution to the equation: {x:.2f}")
linear_eq()