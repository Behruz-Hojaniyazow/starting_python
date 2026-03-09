numbers = list(range(0, 101, 5))
numbers_5 = []
for number in numbers:
    if number % 5 == 0: # Bu yerda % qoldiqni tekshiradi
        numbers_5.append(number)
print(numbers_5)
print(f"{len(numbers_5)}")
