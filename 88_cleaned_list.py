def cleaned_list(elements):
  """a function that cleans the list"""
  clean_list = []
  for element in elements:
    if element not in clean_list:
      clean_list.append(element)
  return clean_list
clean = []
while True:
  choice = input("Enter an element: ").lower()
  clean.append(choice)
  answer = input("Do you want to stop? (yes/no)").lower()
  if answer == 'yes':
    break
result = cleaned_list(clean)
print(f"This is the cleaned list: {result}")