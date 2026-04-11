def component_reader():
  """a function that reads KRYOS spare parts list from file"""
  filename = 'kryos_parts.txt'
  print("\n---KRYOS Inventory System: Reading Data...---")
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      if lines:
        print(f"\nFound {len(lines)} entries in the system:\n")
        for index, line in enumerate(lines, start=1):
          clean_line = line.strip()
          print(f"{index}. {clean_line}")
      else:
        print("The file is empty")
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found, Please run the Writer first")
if __name__ == "__main__":
  component_reader()