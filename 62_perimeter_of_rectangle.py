def get_number(string):
  while True:
    try:
      number = float(input(string))
      if number > 0:
        return number
      else:
        print("Error, The number must be positive, (greater than '0')")
    except ValueError:
      print("Please enter only numbers, Try again")
def perimeter():
  """ a function that finds the perimeter of rectangle"""
  a = get_number("Enter the 'a': ")
  b = get_number("Enter the 'b': ")
  p = 2 * (a + b)
  print(f"Perimeter of rectangle is equal to {p}")
perimeter()