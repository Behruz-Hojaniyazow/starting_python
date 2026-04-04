def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers")
def find_average(*args):
  """a function that calculates the average of the given numbers"""
  if not args:
    return 0
  average = sum(args) / len(args)
  return average
def main():
  numbers = []
  while True:
    num = get_number("Enter a number: ")
    numbers.append(num)
    if input("Will you add another number? (yes/no)").lower().strip() == 'no':
      break
  if numbers:
    result = find_average(*numbers)
    print(f"The average of the given numbers is {result}")
  else:
    print("No numbers entered")
if __name__ == "__main__":
  main()