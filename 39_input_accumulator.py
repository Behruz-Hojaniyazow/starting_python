names = []
print("\nWelcome to our project \n (type 'exit' or 'quit' to leave the project)")

while True:
  user_input = input("enter a name: ")
  
  if user_input.lower() in ['exit', 'quit']:
    print("Thank you for using our project")
    break
  else:
    names.append(user_input)
length_names = len(names)
print(f"There are {length_names} names in the list")
    
for name in names:
    print(f"{name.title()}", end=",")