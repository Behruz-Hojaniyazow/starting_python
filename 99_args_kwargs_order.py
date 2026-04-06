def get_number(prompt):
  """a function that accepts only integers from the user"""
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Please enter only integers, try again")
def infos(age, *args, **kwargs):
  """a function that shows you how to order args and kwargs"""
  if not infos:
    return []
  user_info = []
  age = get_number("Enter your age: ")
  user_info.append(age)
  additionals = []
  while True:
    print("type 'stop' to finish")
    additional = input("What is your hobbies: ").title()
    if additional == 'Stop':
      break
    additionals.append(additional)
  future_plans = {}
  while True:
    print("type 'stop' to finish")
    plan = input("What is your future plans?").title()
    if plan == 'Stop':
      break
    value = get_number("How much money can you earn? ")
    future_plans[plan] = value
  return user_info, additionals, future_plans
def main():
  age_info = infos(user_info)
  hobbies = infos(additionals)
  plans = infos(future_plans)
  print("=" * 30)
  print("Here is the information of the user")
  print("="  * 30)
  print(f"Your are {age_info} years old")
  print(f"Additional infos: {hobbies}")
  for key, value in plans.items():
    print(f"{key} | {value}")
if __name__ == "__main__":
  main()