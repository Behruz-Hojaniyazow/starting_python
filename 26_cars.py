cars = {"Aura" : 0,
      "Phantom" : 3,
      "Nexus" : 0,
      "Apex" : 7,
      "Vanguard" : 6,
      "Horizon" : 10,
      "Bastion" : 9
}
while True:
  customer = input("Which model do you want to buy? (type 'exit' to stop)").title()
  
  # 1. first we check if the user is gonna exit
  if customer == 'Exit':
    print("\nRemaining cars database: ")
    print(cars) # We display the entire dictionary itself on the screen
    break
    
  if customer in cars:
# 2. we check if the customer in our dictionary

    if cars[customer] > 0:
      # 3. we check if the remaining cars are more than 0
      cars['customer'] -= 1
      print(f"Congratulations on your purchase")
    else:
      print(f"Sorry, {customer} is out of stock")
  else:
    # 4.we check if the customer wants to buy the car which does not have in out dictionary
    print(f"We do not sell {customer} here")