import sys

try:
    num1 = float(input("Masukkan angka pertama: "))
except ValueError:
    print("Error: Input pertama bukan angka.")
    sys.exit(1)

try:
    num2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Error: Input kedua bukan angka.")
    sys.exit(1)

operator = input("Masukkan operator (+, -, *, /): ")

if operator not in ['+', '-', '*', '/']:
    raise Exception("Operator tidak valid. Hanya +, -, *, / yang diperbolehkan.")

try:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    print(f"Hasil: {result}")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")