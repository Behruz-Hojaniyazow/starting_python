warehouse = {
	"apple" : 50,
	"banana" : 10,
	"lemon" : 0,
	"pineapple" : 20,
	"cherry" : 9
}
print("the products we have".title())
print("*" * 30)
for i in range(3):
	item = input(f"what kind of fruit do you need ?").lower()
	if item in warehouse:
		amount = warehouse[item]
		if amount == 0:
			print(f"Sorry, {item} is out of stock.")
		elif amount >= 10:
			print(f"We have as much of {item} as you want.")
		else:
			print(f"{item} is in short supply, order quickly")
	else:
			print(f"Sorry, We don't have {item}")