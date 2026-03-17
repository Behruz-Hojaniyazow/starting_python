# 1. Ma'lumotlar bazasini (lug'atni) yaratamiz
students = {
    "Behruz": [5, 5, 4, 5],
    "Ali": [3, 4, 2, 4],
    "Vali": [4, 5, 5, 4]
}

print("Talabalarning o'rtacha ballari:")
print("-" * 30)

# 2. Lug'atni aylanamiz
for name, grades in students.items():
    # grades — bu bizning listimiz (masalan: [5, 5, 4, 5])
    
    # 3. O'rtacha ballni hisoblaymiz
    yigindi = sum(grades) # Ro'yxatdagi hamma sonlar yig'indisi
    fanlar_soni = len(grades) # Ro'yxatda nechta son borligi
    o_rtacha = yigindi / fanlar_soni
    
    # 4. Natijani chiqaramiz (nuqtadan keyin 1 ta raqam bilan)
    print(f"{name}: {o_rtacha:.1f} ball")