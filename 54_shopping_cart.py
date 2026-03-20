print("\nWelcome to our market")
print("\nType 'Stop' to stop the project, Type 'Check' to clarify your purchase")
products = {"Aura" : 50000,
            "Nexus" : 40000,
            "Apex" : 45000,
            "Vanguard" : 47000,
            "Camry" : 25000,
            "Sportage" : 20000,
            "Sonata" : 23000
}
total_sum = []
overall_cost = 0
while True:
  customer = input("Which model do you need? ").strip().title()
  if customer in products:
    value = products[customer]
    total_sum.append(value)
    print(f"{customer} car costs ${value}")
    print(f"{customer} car was added to your purchase")
  elif customer == 'Check':
    overall_cost = sum(total_sum)
    removed_item = total_sum.pop()
    overall_cost -= removed_item
    print(f"Your total purchase cost ${overall_cost}")
      
  elif customer == 'Stop':
    print("Thank you for using our market")
    break
  else:
    print(f"Unfortunately, We do not have {customer} car")
    
print(f"The cars overall value is equal to ${overall_cost}")