def filter_dict(**kwargs):
  """a function that filters the dict"""
  if kwargs:
    clean_data = {}
    for key, value in kwargs.items():
      if isinstance(value, (int, float)):
        clean_data[key] = value
  return clean_data
def main():
  filtered_data = {}
  while True:
    print("type 'stop' to finish")
    kwargs_key = input("Type of information? ").strip()
    if kwargs_key.lower() == 'stop':
      break
    kwargs_value = input(f"Enter the value of {kwargs_key}: ").strip()
    try:
      if '.' in kwargs_value:
        final_value = float(kwargs_value)
      else:
        final_value = int(kwargs_value)
    except ValueError:
      final_value = kwargs_value
    filtered_data[kwargs_key] = final_value
  result = filter_dict(**filtered_data)
  print("\n" + "=" * 30)
  print("FILTERED ELEMENTS (Only numbers):")
  print("=" * 30)
  if result:
    print("\n" + "~" * 30)
    for key, value in result.items():
      print(f"  - {key.capitalize()} | {value}")
    print("~" * 30)
  else:
    print("No information entered")
if __name__ == "__main__":
  main()