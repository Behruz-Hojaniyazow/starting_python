#_1 creatin a function
def incubator_reader():
  #_writing docstring to understand the function easily
  """function that reads the info from the file 'temperature_cond.txt' file"""
  print("\n---Welcome---\n")
  #_entering the filename that you created
  filename = 'incubator_cond.txt'
  #_using try...except to ensure the mistakes
  try:
    with open(filename, 'r' ,encoding = 'utf-8') as file:
      numbers = [float(line.strip()) for line in file]
      if not numbers:
        print("The file is empty")
        return
      print("=" * 30)
      for num in numbers:
        clean_temp = int(num) if num.is_integer else num
      for temp in clean_temp:
        if temp > 37.8:
          print(f"️🧯 {temp}° is high,you must decrease the temperatue")
        if temp == 37.8:
          print(f"✅️ {temp}° is the best temperature for incubator")
        else:
          print(f"🥶 {temp}° temperatue is low, you must increase the temperature")
      print(f"🔎 {len(clean_temp)} incubator info were found")
  except FileNotFoundError:
    print(f"The file '{filename}' was not found, Please run the Writer first")
  except ValueError:
    print("Error: The file contains invalid numerical data")
  except Exception as e:
    print(f"An error occured.- {e}")
if __name__ == "__main__":
  incubator_reader()