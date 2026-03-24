def find_even(numbers):
  evens = []
  for num in numbers:
    if num % 2 == 0:
      evens.append(num)
  return evens
num_list = [12, 35, 67, 23, 20, 48]
result = find_even(num_list)
print(f"These are even numbers {result}")