def defining_prime(number):
  """a function that defines whether the number prime or composite"""
  if number <= 1:
    return "neither prime nor complex"
  for i in range(2, number):
    if number % i == 0:
      return "composite"
      
  return "prime"
  
while True:
  try:
    num = int(input("Enter only integer numbers (enter a letter to exit): "))
  except ValueError:
    print("The project was ended, God bless you")
    break
  result = defining_prime(num)
  print(f"{num} is a {result} number")
  choice = input("Do you want to check a number again? (yes/no) ")\.lower()
  if choice == 'no':
    print("Good Bye")
    break