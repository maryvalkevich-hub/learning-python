"""
Exam Training — Conditional & Logical Operators
Date: 27 June 2026
Topics: if/elif/else, and/or/not, nested conditions, edge cases
Result: 20 tasks completed (17/20 first attempt, 20/20 after corrections)

Key learnings:
- Negative numbers with // and % (Python rounds DOWN, not to zero)
- Priority of conditions (check strictest first)
- Using >= instead of > for permutations with duplicates
- Boolean arithmetic: True + False = 1 in Python
"""
# Задача №20 - Подвох: финальная комплексная. Дано число n (1 ≤ n ≤ 1000). Определи:
  # Если n делится на 3, 5 и 7 — выведи "ALL"
  # Если n делится только на два из них — выведи "TWO"
  # Если n делится только на одно из них — выведи "ONE"
  # Если не делится ни на одно — выведи "NONE"
num = int(input())
d3 = num % 3 == 0
d5 = num % 5 == 0
d7 = num % 7 == 0
count = d3 + d5 + d7  # True = 1, False = 0 в Python!
if count == 3:
    print("ALL")
elif count == 2:
    print("TWO")
elif count == 1:
    print("ONE")
else:
    print("NONE")

  # Задача №19 - Дано трёхзначное число. Выведи число, образованное перестановкой цифр в порядке убывания (например, 314 → 431).
num = int(input())
a = num // 10 ** 2
b = (num // 10) % 10
c = num % 10
if a >= b >= c:
    print(a, b, c, sep="")
elif a >= c >= b:
    print(a, c, b, sep="")
elif b >= a >= c:
    print(b, a, c, sep="")
elif b >= c >= a:
    print(b, c, a, sep="")
elif c >= a >= b:
    print(c, a, b, sep="")
elif c >= b >= a:
    print(c, b, a, sep="")

  # Задача №18 - Подвох: логические операторы. Что выведет код?
  # x = 15
  # if x > 10 and x < 20 or x == 25:
  #    print("A")
  # elif x > 5 and not (x % 2 == 0):
  #    print("B")
  # else:
  #    print("C") - Ответ - A

  # Задача №17 - Подвох: комплексная задача. Дано четырёхзначное число. Проверь:
  # Сумма первых двух цифр равна сумме последних двух цифр
  # Число делится на 7
  # Если оба условия выполняются — выведи "LUCKY", иначе — "UNLUCKY".
num = int(input())
digit1 = num // 10 ** 3
digit2 = (num // 10 ** 2) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
if (digit1 + digit2 == digit3 + digit4) and (num % 7 == 0):  # Это с условием что число делится на 7 без остатка
    print("LUCKY")
else:
    print("UNLUCKY")

  # Задача №16 - Подвох: шахматная доска. Даны координаты двух клеток шахматной доски (от 1 до 8). Определи, могут ли они быть атакованы слоном за один ход. Выведи "YES" или "NO".
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x2 - y2 == x1 - y1 or x1 - x2 == y2 - y1:
    print("YES")
else:
    print("NO")

  # Задача №15 - Подвох: вложенные условия. Даны три числа. Определи, сколько из них равны между собой. Выведи:
  # "Все различны" — если все три разные
  # "Два равны" — если два равны
  # "Все равны" — если все три равны
a, b, c = int(input()), int(input()), int(input())
if a != b and b != c and a != c:
    print("Все различны")
elif a == b == c:
    print("Все равны")
else:
    print("Два равны")

  # Задача №14 - Подвох: приоритет операций - Что выведет код? Напиши ответ.
  # a = 15 // (7 % 3)
  # b = 2 ** 3 * 2
  # c = 10 % 3 + 5
  #print(a + b + c) - Ответ: 37

  # Задача №13 - Дано число n (может быть отрицательным). Выведи результат n // 5 и n % 5. Проверь на n = -13.
num = int(input())
print(num // 5)
print(num % 5)

  # Задача №12 - Дано число от 1 до 99. Выведи, сколько в нём десятков и единиц (например, 45 → "4 десятка, 5 единиц").
num = int(input())
digit1 = num // 10
digit2 = num % 10
print(f"В {num} - {digit1} десятка, {digit2} единиц")

  # Задача №11 -  Даны три стороны треугольника. Определи, является ли он равносторонним, равнобедренным или разносторонним. Выведи соответствующее сообщение.
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

  # Задача №10 - Дано число. Определи, к какому диапазону оно принадлежит: 0-10: "A" 11-20: "B" 21-30: "C" Вне диапазона: "Error"
num = int(input())
if 0 <= num <= 10:
    print("A")
elif 11 <= num <= 20:
    print("B")
elif 21 <= num <= 30:
    print("C")
else:
    print("Error")

  # Задача №9 - Дано число секунд. Определи, сколько это полных часов, минут и секунд. Выведи время в формате "HH:MM:SS" (например, 3665 секунд = 01:01:05).
num = int(input())
HH = num // 60 ** 2
MM = (num // 60) % 60
SS = num % 60
print(f"{HH:02d}:{MM:02d}:{SS:02d}")  

  # Задача №8 - Даны координаты двух точек на плоскости. Определи, могут ли они быть вершинами прямоугольника с сторонами, параллельными осям координат. Выведи "YES" или "NO".
x, y, x1, y1 = int(input()), int(input()), int(input()), int(input())
if (x1 == x and (y1 < y or y < y1)) or (y1 == y and(x1 < x or x < x1)):
    print("YES")
else:
    print("NO")

  # Задача №7 - Дано трёхзначное число. Проверь, есть ли в нём одинаковые цифры. Выведи "YES" или "NO".
num = int(input())
digit1 = num // 10 ** 2
digit2 = (num // 10) % 10
digit3 = num % 10
if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print("YES")
else:
    print("NO")

  # Задача № 6 - Даны три числа. Определи, сколько из них положительных. Выведи количество.
a, b, c = int(input()), int(input()), int(input())
if (a < 0 and b < 0 and c > 0) or (a < 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c < 0):
    print(1)
elif (a < 0 and b > 0 and c > 0) or (a > 0 and b > 0 and c < 0) or (a > 0 and b < 0 and c > 0):
    print(2)
elif (a > 0 and b > 0 and c > 0):
    print(3)

  # Задача №5 - Дано число. Если оно делится на 3 и не делится на 5 — выведи "Fizz", если делится на 5 и не делится на 3 — выведи "Buzz", если делится и на 3, и на 5 — выведи "FizzBuzz", иначе — само число.
num = int(input())
if (num % 3 == 0) and not (num % 5 == 0):
    print("Fizz")
elif (num % 5 == 0) and not (num % 3 == 0):
    print("Buzz")
elif (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
else:
    print(num)

  # Задача №4 - Дано число. Проверь, является ли оно чётным и трёхзначным одновременно. Выведи "YES" или "NO".
num = int(input())
if 100 <= num <= 999 and num % 2 == 0:
    print("YES")
else:
    print("NO")

  # Задача №3 -  Даны два числа. Выведи наибольшее из них. Используй только if/else (без функции max).
a, b = int(input()), int(input())
if a > b:
    print(a)  # Решение при условии, что a != b
else:
    print(b)

  # Задача №2 - Дано число от 1 до 7. Выведи название дня недели (1 — Monday, 2 — Tuesday и т.д.). Если число вне диапазона — выведи "Error".
num = int(input())
if num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
elif num == 7:
    print("Sunday")
else:
    print("Error")      

  # Задача №1 - Дано число. Если оно положительное — выведи "Positive", если отрицательное — "Negative", если ноль — "Zero".
num = int(input())
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")
