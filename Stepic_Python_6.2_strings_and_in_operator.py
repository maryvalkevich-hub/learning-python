"""
Stepik Tasks — String Methods & 'in' Operator
Date: 07 July 2026
Topics: len(), f-strings, concatenation, 'in' operator, substring search
Result: 8 tasks completed (5 string tasks + 3 'in' operator tasks)

Notable solutions:
- Task #5: Arithmetic progression of string lengths using max/min/sum trick
- Task #8: Email validation using 'in' operator
- Task #7: Weekend check using variables for substrings
"""

  # Задача №8 - Корректный email 📧.Будем считать email адрес корректным, если в нём есть символы собачки (@) и точки (.). Напишите программу, проверяющую корректность email адреса.
  # Программа должна вывести строку «YES» (без кавычек), если email адрес является корректным, или «NO» (без кавычек) в противном случае.
  # Примечание. Для настоящих email адресов недостаточно наличия символов @ и ., однако их отсутствие гарантировано влечёт за собой неверный email.
a = input()
if "@" in a and "." in a:
    print("YES")
else:
    print("NO")

  # Задача №7 - Отдыхаем ли? 😎Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.
a = input()
s, s1 = "суббота", "воскресенье"
if (s in a) or (s1 in a):
    print("YES")
else:
    print("NO")

  # Задача №6 - Цвет настроения синий 🟦.Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «синий», или «NO» (без кавычек) в противном случае.
a = input()
s = "синий"
if s in a:
    print("YES")
else:
    print("NO")

  # Задача №5 - Арифметические строки. Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.
  # Формат выходных данных: Программа должна вывести строку «YES» (без кавычек), если из длин введённых слов можно построить арифметическую прогрессию, или «NO» (без кавычек) в противном случае.
a, b, c = input(), input(), input()
a1, b1, c1 = len(a), len(b), len(c)
d = max(a1, b1, c1)
f = min(a1, b1, c1)
e = (a1 + b1 + c1) - (d + f)
if e - f == d - e:
    print("YES")
else:
    print("NO")

  # Задача №4 - Три города 🏙️.Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
  # Примечание. Гарантируется, что длины названий всех трёх городов различны.
a, b, c = input(), input(), input()
a1, b1, c1 = len(a), len(b), len(c)
d = max(a1, b1, c1)
f = min(a1, b1, c1)
if a1 != d and a1 != f:
    if b1 > c1:
        print(c, b, sep = "\n")
    elif c1 > b1:
        print(b, c, sep = "\n")
elif b1 != d and b1 != f:
    if a1 > c1:
        print(c, a, sep = "\n")
    elif c1 > a1:
        print(a, c, sep = "\n")
elif c1 != d and c1 != f:
    if a1 > b1:
        print(b, a, sep = "\n")
    elif b1 > a1:
        print(a, b, sep = "\n")

  # Задача №3 - Футбольная команда ⚽.Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит информацию о ней в следующем формате:
  # Футбольная команда <название футбольной команды> имеет длину <длина названия футбольной команды> символов
name = input()
s = len(name)
print(f"Футбольная команда {name} имеет длину {s} символов")

  # Задача №2 - What's Your Name?Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя – и выводит фразу:
  # Hello <введённое имя> <введённая фамилия>! You have just delved into Python
name, surname = input(), input()
print(f"Hello {name} {surname}! You have just delved into Python")  # Я бы написала так, но в Stepic так нельзя...

s1 = "Hello "   # А это вариант для Stepic
s2 = name + " " + surname
s3 = "! You have just delved into Python"
s = s1 + s2 + s3
print(s)

  # Задача №1 - Напишите программу, которая выводит текст: "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
  # Примечание. Используйте конкатенацию строк.
print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')
