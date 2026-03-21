products = {
    "Aura": 50000, "Nexus": 40000, "Apex": 45000,
    "Vanguard": 47000, "Camry": 25000, "Sportage": 20000, "Sonata": 23000
}

cart = []  # Savatchaga mahsulot nomlarini yigamiz
print("\n--- Welcome to Our Car Market ---")
print("Commands: 'Stop' to finish, 'Check' to see your cart")

while True:
    choice = input("\nWhich model do you need? ").strip().title()

    if choice == 'Stop':
        break
    
    elif choice == 'Check':
        if not cart:
            print("Your cart is empty!")
            continue
        
        print("\n--- Your Current Cart ---")
        total = 0
        for item in cart:
            price = products[item]
            total += price
            print(f"- {item}: ${price:,}")
        print(f"TOTAL COST: ${total:,}")
        print("-" * 30)

    elif choice in products:
        cart.append(choice)
        print(f"{choice} added to your purchase.")
    
    else:
        print(f"Unfortunately, we do not have {choice} car.")

# Final hisob
final_total = sum(products[item] for item in cart)
print(f"\nFinal purchase completed! Total amount: ${final_total:,}")
print("Thank you for using our market!")