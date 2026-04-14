def parse_number(text):
    """Kasr ko'rinishidagi matnni (masalan '2/3') songa aylantiradi"""
    try:
        if '/' in text:
            surat, mahraj = text.split('/')
            return float(surat) / float(mahraj)
        return float(text) if text else 0.0
    except:
        return 0.0

def solve_complex_pro():
    print("\n--- Kasrli Kompleks sonlar kalkulyatori ---")
    
    count = int(input("Nechta kompleks son bor? (masalan, 2): "))
    total_real = 0.0
    total_imaginary = 0.0

    for i in range(1, count + 1):
        print(f"\n{i}-son uchun:")
        
        multiplier = 1
        if i > 1:
            op = input(f"Oldidagi ishora (+ yoki -): ").strip()
            if op == "-": multiplier = -1

        # Endi bu yerda '2/3' deb yozish mumkin
        real_input = input(f"  Haqiqiy qismi (masalan 2/3 yoki 5): ")
        imag_input = input(f"  Mavhum qismi (i oldidagi son, masalan 1/5): ")

        total_real += parse_number(real_input) * multiplier
        total_imaginary += parse_number(imag_input) * multiplier

    # Natijani chiqarish
    sign = "+" if total_imaginary >= 0 else "-"
    print("\n" + "="*40)
    print(f"YAKUNIY JAVOB: {round(total_real, 4)} {sign} {round(abs(total_imaginary), 4)}i")
    print("="*40)

if __name__ == "__main__":
    solve_complex_pro()