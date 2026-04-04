def find_longest_word(*args):
  """a function that finds the longest words"""
  longest_length = 0
  longest_words = []
  for word in args:
    if len(word) > longest_length:
      longest_words = [word]
      longest_length = len(word)
    elif len(word) == longest_length:
      longest_words.append(word)
  return longest_words, longest_length
def main():
  words = []
  while True:
    print("type (stop) to finish")
    user_input = input("Enter a word: ").lower().strip()
    if user_input == "stop":
      break
    if user_input:
      words.append(user_input)
  if words:
    print("\n---Longest Words---")
    result, length = find_longest_word(*words)
    for r in result:
      print(f"{r} | {length} letters")
  else:
    print("No information entered")
if __name__ == "__main__":
  main()