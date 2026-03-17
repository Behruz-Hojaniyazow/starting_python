#imagine in our account has $10000
account = 10000

while True:
  user_input = input("How much money would you like to withdraw from you account? \n ('type 'exit to leave the project')")
  
  if user_input.lower() == 'exit':
    print("\nThanks for using our bank, GoodBye")
    break
  try:
    bank = float(user_input)
  
    if bank > account:
      print("\nYou don't have that much money in your account")
    else:
      account -= bank
      print(f"\nSuccess, You have ${account} left in your account")
    if account == 0:
      print("\nYou're out of money !")
      break
  
  except ValueError:
    print("\nPlease enter only numbers")
    
print(f"\nFinal Balance: ${account}, Project is over")