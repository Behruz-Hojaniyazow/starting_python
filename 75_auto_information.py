def auto_info(model, year, colour, cost):
  auto = {"model" : model,
        "year" : year,
        "colour" : colour,
        "cost" : cost
}
  return auto
cars = []
while True:
  model = input("Enter the model: ")
  year = input(f"Enter {model}'s year: ")
  colour = input(f"Enter {model}'s colour: ")
  cost = input(f"Enter {model}'s cost: ")
  cars.append(auto_info(model, year, colour, cost))
  answer = input("Do you want to add more cars? (yes/no)") \
  .strip().lower()
  if answer == 'no':
    break
print("\nCars in our showroom")
for car in cars:
  print(f"{car['model'].title()} {car['colour'].title()} colour,made in {car['year']}, and it costs ${car['cost']}")