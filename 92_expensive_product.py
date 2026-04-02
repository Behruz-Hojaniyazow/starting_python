def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers, Try again")
def get_expensive(products):
  """a function that finds the most expensive products in the dict"""
  max_price = max(products.values())
  most_expensives = {name: cost for name, cost in products.items() if cost == max_price}
  return max_price, most_expensives
fruits = {}
while True:
  fruit = input("Enter a fruit: ").title()
  cost = get_number(f"Enter {fruit}'s price: ")
  fruits[fruit] = cost
  if input("Shall we add more fruits or that's enough (yes/no)?").lower() == 'no':
    break
expensive_cost, expensive_fruit = get_expensive(fruits)
print("-" * 30)
print(f"\nThe most expensive price is ${expensive_cost}")
print("=" * 30)
for name, cost in expensive_fruit.items():
  print(f"The most expensive fruit is {name}, it costs ${cost}")
  print("=" * 30)