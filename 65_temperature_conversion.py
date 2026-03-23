def get_number(string):
  while True:
    try:
      return float(input(string))
    except ValueError:
      print("Please, Enter only numbers")
      
def celsius_to_fahrenheit():
  """a function that converts a given temperature in celsius to fahrenheit"""
  c = get_number("Enter a number for 'C' : ")
  f = c * 1.8 + 32
  print(f"The temperature was converted to fahrenheit ({f}°C)")
celsius_to_fahrenheit()
  