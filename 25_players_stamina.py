player = 100

while True:
  spent_stamina = float(input("How long have you been playing football ?: "))
  player -= spent_stamina
  
  if player < 0:
    player = 0
    
  print(f"I have %{player} stamina left")
  
  if player <= 20:
    break
  
print("The player is tired, take a backup.")