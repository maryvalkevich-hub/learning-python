"""
Stepik Exam #1 — Integer Arithmetic
Date: 16 June 2026
Result: 10/10 tests + 4/4 tasks passed in 50 minutes

Topics covered:
- input() / print() / sep / end
- Variables, PEP8
- Integer arithmetic: +, -, *, **, //, %
- Digit extraction algorithms
- Priority of operations
"""

# Задача 1: Прямоугольник из звёздочек (4×17)
print("*" * 17)
print("*", "*", sep=" " * 15)
print("*", "*", sep=" " * 15)
print("*" * 17)

# Задача 2: Квадрат суммы и сумма квадратов
a = int(input())
b = int(input())
print("Квадрат суммы", a, "и", b, "равен", (a + b) ** 2)
print("Сумма квадратов", a, "и", b, "равна", a ** 2 + b ** 2)

# Задача 3: a^b + c^d
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a ** b + c ** d)

# Задача 4: n + nn + nnn
n = int(input())
print(n + (10 * n + n) + (100 * n + 10 * n + n))
