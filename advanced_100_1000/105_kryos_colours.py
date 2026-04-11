def kryos_colors():
  """funcion that chooses the best colors for kryos auto cars"""
  colors = []
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}, Choose the best color for KRYOS cars---")
  filename = "colors.txt"
  print("=" * 30)
  print("Type (stop) to finish")
  print("=" * 30)
  while True:
    color = input("Choose a color for KRYOS cars: ")
    if color.lower() == 'stop':
      break
    colors.append(color)
  if colors:
    with open (filename, 'w', encoding = 'utf-8') as file:
      for color in colors:
        file.write(f"{color.upper()}\n")
    if len(colors) > 1:
      print(f"\n(!){len(colors)} colors were added successfully to the '{filename}'")
    else:
      print(f"\n(!){len(colors)} color was added successfully to the '{filename}'")
  else:
      print("No colors were added, File was not created")
if __name__ == "__main__":
  kryos_colors()