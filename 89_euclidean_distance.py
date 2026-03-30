import math
def get_number(prompt):
  """a function that only accepts integers from the user"""
  while True:
    try:
      #for calculating and AI it's better to use float
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers, Try again")
      
def find_distance(x1, y1, x2, y2):
  """a function that finds the euclidean distance"""
  #euclidean formula
  d = math.sqrt((x2 - x1 )**2 + (y2 - y1)**2)
  return d
  
#---Main Part---
print("\nEnter the coordinates of point 1")
x1 = get_number("x1 = ")
y1 = get_number("y1 = ")

print("\nEnter the coordinates of point 2")
x2 = get_number("x2 = ")
y2 = get_number("y2 = ")

result = find_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between these points is {result:.2f}")