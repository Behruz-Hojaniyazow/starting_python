def neoplan_reader():
  """function that reads the projects from the 'neoplan_projects.txt' file"""
  filename = 'neoplan_projects.txt'
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}!---")
  try:
    with open(filename, 'r', encoding = 'utf-8') as file:
      lines = file.readlines()
      if lines:
        for index, line in enumerate(lines, start = 1):
          clean_line = line.strip()
          print(f"Project - {index}, {clean_line}")
        print(f"\n(!){len(lines)} projects were found\n")
      else:
        print("The File was empty")
  except FileNotFoundError:
    print("Error, '{filename}' was not found, Please run the Writer first")
if __name__ == "__main__":
  neoplan_reader()