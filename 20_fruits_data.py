fruits = {"banana" : 5000, "apple" : 2000, "grapes" : 870, "watermelon" : 1200}
query = input("What kind of fruit do you need ?").lower()
if query in fruits:
	print(f"Yes, we have {query} and it costs {fruits[query]}, How much do you want ?")
else:
	print(f"Sorry, Unfortunately we don't have {query}")
for fruit in fruits:
	print(f"{fruit} costs {fruits[fruit]}")
print("and these are the products we have")