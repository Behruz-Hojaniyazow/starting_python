def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers")
def max_num(a, b, c):
  """a function that finds the maximum number"""
  if a >= b and a >= c:
    return a
  elif b >= a and b >= c:
    return b
  else:
    return c
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
num3 = get_number("Enter the second third number: ")
result = max_num(num1, num2, num3)
print("=" * 30)
print(f"The biggest number is | {result}")
print("=" * 30)