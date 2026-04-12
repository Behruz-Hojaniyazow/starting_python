def neoplan_project():
  """function that accepts projects from the user"""
  filename = "neoplan_projects.txt"
  name = input("Please, Enter your name: ")
  print(f"\n---Welcome {name.title()}!---\n")
  projects = []
  print("Type 'stop' to finish")
  while True:
    project = input("Enter the architectural project: ")
    if project.lower() == 'stop':
      break
    projects.append(project)
  if projects:
    with open(filename, 'w', encoding = 'utf-8') as file:
      for project in projects:
        file.write(f"{project.upper()}\n")
    print(f"{len(projects)} projects were added to the '{filename}'")
  else:
    print("No info entered, File was not created")
if __name__ == "__main__":
  neoplan_project()