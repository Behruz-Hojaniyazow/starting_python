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
    num = int(input("Enter only integer numbers: "))
    break
  except ValueError:
    print("Please enter only integers, Try again")
result = defining_prime(num)
print(f"{num} is a {result} number")