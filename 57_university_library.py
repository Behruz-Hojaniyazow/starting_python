books = {
    "Python": 3,
    "Math": 5,
    "Physics": 2,
    "Geometry": 0,
    "Literature": 0,
    "Chemistry": 4
}
basket = {}  # sold_book o'rniga "basket" (savat) desak tushunarliroq

# 1. Dastlabki holatni chiroyli qilib ekranga chiqaramiz
print("\n--- Current library's status ---")
for book, amount in books.items():
    print(f"{book}: {amount}")
print("-" * 30)

while True:
    print("\n[Commands: type 'Return' to return a book, 'Bye' to stop]")
    
    # Foydalanuvchining nima xohlayotganini soraymiz
    action = input("Which book do you need? (or enter command): ").strip().title()

    # 1-QADAM: Chiqib ketish mantigi
    if action == 'Bye':
        break

    # 2-QADAM: Kitob qaytarish mantigi
    elif action == 'Return':
        returned_b = input("Which book are you returning? ").strip().title()
        value = int(input(f"How many '{returned_b}' books are you going to return? "))
        
        # Kutubxonaga kitobni qoshamiz
        if returned_b in books:
            books[returned_b] += value
        else:
            books[returned_b] = value # Agar umuman yangi kitob bersa, ro'yxatga qoshadi
            
        print(f"Thank you! {value} '{returned_b}' added back to the library.")

    # 3-QADAM: Kitob olish mantigi
    elif action in books:
        value = int(input(f"How many '{action}' books do you need? "))
        
        # Zaxirada yetarlimi? Shuni tekshiramiz!
        if books[action] >= value:
            books[action] -= value
            
            # Savatga qoshish mantigi (oldin shu kitob olingan bolsa, ustiga qoshadi)
            basket[action] = basket.get(action, 0) + value 
            print(f"Success! {value} '{action}' book(s) added to your basket.")
        else:
            # Agar kitob yetishmasa:
            print(f"Sorry, we only have {books[action]} '{action}' book(s) left in stock.")

    # 4-QADAM: Notogri narsa kiritsa
    else:
        print("Sorry, we don't have this book.")

# TSikl tugagach (Bye yozilgach), savatni va kutubxonaning yangi holatini korsatamiz
print("\n--- Thank you for using our library ---")

print("\n--- In Your Basket ---")
if basket:
    for book, value in basket.items():
        print(f"{value} {book} book(s)")
else:
    print("You didn't buy any books.")

print("\n--- Updated Library Status ---")
for book, value in books.items():
    print(f"{book}: {value} left")
