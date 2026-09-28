"""
Stepik: Python Programming
Topic: Nested Loops — Pattern Generation and Matrix Logic
Date: 07 August 2026
Status: Completed ✅

Tasks solved: 5 (Таблица-1, Таблица-2, Таблица-3, Численный треугольник 1, Звёздный треугольник 🌶️)
Topics covered:
- Nested `for` loops for 2D pattern generation (rows and columns).
- Dynamic range boundaries dependent on outer loop variables.
- Clean output formatting using f-strings.
- Algorithmic splitting of symmetric patterns (ascending and descending phases).

Notable challenges:
- Task #5 (Звёздный треугольник 🌶️): Successfully implemented a symmetric triangle by calculating the midpoint (`n = num // 2`) and using two separate loop blocks for the ascending and descending halves. This ensured precise control over the output shape without complex conditional logic inside a single loop.

Personal note: Solved these while managing extreme heat and a busy household. The strict, predictable logic of nested loops requires mental discipline, which serves as a good, calming anchor amidst daily chaos.
"""

  # Задача №1 - Таблица-1.
  # Дано натуральное число n(n≤9). Напишите программу, которая печатает таблицу размером n×3, состоящую из данного числа (числа отделены одним пробелом).
  # Примечание. В конце строки может быть пробел.
num = int(input())
for _ in range(num):
    for _ in range(3):
        print(num, end = " ")
    print()

  # Задача №2 - Таблица-2.
  # Дано натуральное число n(n≤9). Напишите программу, которая печатает таблицу размером n×5, где в i-ой строке указано число i (числа отделены одним пробелом).
num = int(input())
for i in range(1, num + 1):
    for j in range(5):
        print(i, end = " ")
    print()

  # Задача №3 - Таблица-3.
  # Дано натуральное число n(n≤9). Напишите программу, которая печатает таблицу сложения для всех чисел от 1 до n (включительно) в соответствии с примером.
  # Примечание 1. Таблицу сложения подразумеваем от 1 до 9 (включительно).
num = int(input())
for i in range(1, num + 1):
    for j in range(1, 10):
        print(f"{i} + {j} = {i + j}")
    print()


  # Задача №4 - Численный треугольник 1.
  # Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
  # 1
  # 22
  # 333
  # 4444
  # 55555
  # ...
num = int(input())
for i in range(1, num + 1):
    for _ in range(i):
        print(i, end = "")
    print()

  # Задача №5 - Звёздный треугольник 🌟🌶️.
  # Дано нечётное натуральное число n. Напишите программу, которая печатает равнобедренный звёздный треугольник с основанием, равным n, в соответствии с примером:
  # *
  # **
  # *** 
  # ****
  # ***
  # **
  # *
num = int(input())
n = num // 2
for i in range(0, n + 1):
    for _ in range(i + 1):
        print("*", end = "")
    print()
for i in range(n + 1, 0, -1):
    for _ in range(i - 1):
        print("*", end = "")
    print()
