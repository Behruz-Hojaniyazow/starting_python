memory = {"history" : []}
while True:
  try:
    print("\n---Menu---")
    print("1. press 1 to add numbers")
    print("2. press 2 to multiply numbers")
    print("3. press 3 to stop the project")
    choice = int(input("Choose an action (1/2/3)"))
    if choice == 1:
      a = float(input("enter the first number: "))
      b = float(input("enter the second number: "))
      result = a + b
      action_string = f"{a} + {b} = {result}"
      memory['history'].append(action_string)
      print(f"Result: {result}. action was added to memory")
    elif choice == 2:
      a = float(input("enter the first number: "))
      b = float(input("enter the second number: "))
      result = a * b
      action_string = f"{a} × {b} = {result}"
      memory['history'].append(action_string)
      print(f"Result: {result}. action was added to memory")
    elif choice == 3:
      print("The project was stopped")
      print(memory)
      break
    else:
      print("The wrong choice, please choose only 1, 2, or 3")
  except ValueError:
    print("please write only numbers")