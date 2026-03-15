try:
  
	num = float(input("Which number would you like to find the percentage ? "))
	
	percent = float(input(f"What percentage of  {num} do you need ? "))
	
	result = (num / 100) * percent
	
	print(f"{percent}% of {num} is equal to  {result}")
	
except ValueError:
	print("Please enter numbers only")