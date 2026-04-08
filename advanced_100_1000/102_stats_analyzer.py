def get_number(prompt):
  """a function that only accepts numbers from the user"""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Please enter only numbers, try again")
def analyze_stats(**kwargs):
  """a function that analyzes the given stats"""
  if not kwargs:
    return "No information entered"
  max_score = max(kwargs.values())
  top_subject = max(kwargs, key=kwargs.get)
  min_score = min(kwargs.values())
  min_subject = min(kwargs, key=kwargs.get)
  average_score = sum(kwargs.values()) / len(kwargs)
  report = {
          "highest" : (top_subject, max_score),
          "lowest" : (min_subject, min_score),
          "average" : average_score
  }
  return report
def main():
  subject_infos = {}
  user_name = input("Enter your name: ")
  print(f"\n---Welcome {user_name.title()}! Enter subject info---")
  while True:
    print("Type 'stop' to finish")
    key = input("Enter a subject: ")
    if key.lower() == 'stop':
      break
    value = get_number(f"Enter the score of {key}: ")
    subject_infos[key] = value
  if subject_infos:
    result = analyze_stats(**subject_infos)
    print("\n---These are your subject info---")
    print("\n" + "~" * 30)
    for key, value in result.items():
      if isinstance(value, tuple):
        name, score = value
        print(f" -  {key.capitalize()}: {name} {score:.1f}")
      elif isinstance(value, (float, int)):
        print(f" -  {key.capitalize()}: {value:.1f}")
    print("\n" + "~" * 30)
  else:
    print("No info entered")
if __name__ == "__main__":
  main()