expenses = {
	"transport" : [200, 180, 350],
	"foods" : [350, 280, 300],
	"learning" : [60, 100, 80],
	"health" : [30, 10, 45]
}
print("Your total expenses:")
print("☆" * 30)
for expense, costs in expenses.items():
	total_expense = sum(costs)
	print(f"You have spent for {expense}: {total_expense} dollars  ")