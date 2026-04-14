def training_stats():
  """function that displays the saved info in the 'mauy_training.txt' file"""
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}---")
  filename = 'muay_training.txt'
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      if lines:
        print("=" * 30)
        for index, line in enumerate(lines, start = 1):
          clean_line = line.strip()
          print(f"{index}. {clean_line}")
          print("-" * 30)
        if len(lines) > 1:
          print(f"{len(lines)} exercises were found from the '{filename}' file")
        else:
          print(f"\n(!){len(lines)} exercise was found from the '{filename}' file")
      else:
        print("The file was empty")
  except FileNotFoundError:
    print("File was not created, Please run the writer first")
if __name__ == "__main__":
  training_stats()