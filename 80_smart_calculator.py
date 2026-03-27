def smart_calc(num1, num2, operator):
  """a function that takes three arguments and performs a mathematical operation"""
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "×":
    return num1 * num2
  elif operator == "÷":
    if num2 == 0:
      return "Can't divide by zero"
    else:
      return num1 / num2
  else:
    return "Unknown action"
def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
      break
    except ValueError:
      print("Please enter only numbers")
number1 = get_number("Enter the first number: ")
number2 = get_number("Enter the second number: ")
choice = input("Which operator do you need (+/-/×/÷)")
result = smart_calc(number1, number2, choice)
print(f"{number1} {choice} {number2} = {result}")