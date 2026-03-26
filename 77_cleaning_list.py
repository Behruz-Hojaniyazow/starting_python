def unique_elements(all_list):
  """a function that cleans a list"""
  new_list = []
  for item in all_list:
    if item not in new_list:
      new_list.append(item)
  return new_list
fruits = []
while True:
  fruit = input("What kind of fruit do you need? ")
  fruits.append(fruit)
  answer = input("Do you want more fruits? (yes/no)") \
  .strip().lower()
  if answer == 'no':
    break
if fruits:
  clean_list = unique_elements(fruits)
  print(f"\nThis is the cleaned list {clean_list}")
else:
  print("\nThe list is empty")