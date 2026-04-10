def auto_kryos():
  """a function that collects compononents for 'kryos' auto car"""
  components = []
  user_name = input("Enter your name: ")
  print(f"\n---Welcome {user_name.title()} to the Kryos company---\n")
  print("Type (stop) to finish")
  while True:
    compo = input("Insert the compononent part: ")
    if compo.lower() == 'stop':
      break
    components.append(compo)
  if components:
    filename = "kryos_parts.txt"
    with open(filename, 'w', encoding='utf-8') as file:
      file.write("These are the parts of KRYOS auto cars\n")
      for part in components:
        file.write(f"{part.upper()}\n")
    print(f"\n(!) {len(components)} components were successfully saved to '{filename}'.")
  else:
    print("No components were added, File was not created")
if __name__ == "__main__":
  auto_kryos()