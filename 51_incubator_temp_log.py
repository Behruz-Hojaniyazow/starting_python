print("\n---Incubator temperature log")
print("\ntype 'stop' to stop the project")
logs = []
while True:
  entry = input(f"{len(logs) + 1} What is the current temp? ").strip().lower()
  if entry == 'stop':
    break
  try:
    temp = float(entry)
    logs.append(temp)
  except ValueError:
    print("please write only numbers or 'stop' ")
if logs:
  average = sum(logs) / len(logs)
  print(f"\nAverage temperature is {average:.2f}°C")
  print(f"\ntotal number of measurements are {len(logs)}")
else:
  print("\nNo information entered")