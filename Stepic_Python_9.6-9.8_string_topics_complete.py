"""
Stepik: Python Programming
Topic: String Operations — Complete Module
Date: 20 September 2026
Status: Completed ✅

Subtopics covered:
1. String Formatting (Форматирование строк)
2. Unicode & Character Codes (Коды символов)
3. String Comparison (Сравнение строк)

Tasks solved: 19 total
- Formatting: 5 tasks (format(), f-strings, currency rates, math expressions, weight tracking)
- Unicode: 8 tasks (next letter, character range, simple cipher, heaviest word, message cost, letter substitution, system glitch, Caesar cipher)
- Comparison: 6 tasks (magic number, min/max strings, unusual comparison, word sorting, class name validation, book sorting)

Topics covered:
- String formatting: .format() method, f-strings, inline expressions, float formatting (:.2f)
- Unicode: ord(), chr(), character codes, ASCII vs Unicode
- String comparison: lexicographic order, min()/max() for strings, case-insensitive comparison
- Advanced: Caesar cipher, character substitution, multi-level sorting

Notable achievements:
- Mastered compact code writing (one-liners) while maintaining readability.
- Solved complex validation tasks (class names, book sorting) with elegant logic.
- Learned to handle edge cases: empty strings, special characters, case sensitivity.
- Applied iterative problem-solving: from brute-force to optimized solutions.

Personal note: Completed this module while managing migraines, hypoglycemia, and a busy family schedule. Proved that consistent, gentle pacing + proper health management = deep understanding. The "read → rest → consolidate" learning rhythm continues to work beautifully.
"""

# ============================================================================
# ТЕМА 1: ФОРМАТИРОВАНИЕ СТРОК (String Formatting)
# ============================================================================

# Задача №1 - Исторический факт (format())
year = 2010
money_sum = "10k"
type_currency = "Bitcoin"
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, money_sum, type_currency)
print(s)

# Задача №2 - Исторический факт (f-string)
year = 2010
money_sum = "10K"
type_currency = "Bitcoin"
print(f"In {year}, someone paid {money_sum} {type_currency} for two pizzas.")

# Задача №3 - Курсы валют 
date = input()
rate_euro = float(input())
rate_yuan = float(input())
print(f"На {date}: 1€ = {rate_euro}₽, 1¥ = {rate_yuan}₽")

# Задача №4 - Сумма кубов 🆚 Куб суммы
a, b = int(input()), int(input())
print(f"Для чисел {a} и {b}:")
print(f"  Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}")
print(f"  Куб суммы: ({a}+ {b})**3 = {(a + b) ** 3}")

# Задача №5 - (Не) Активное похудение 🏃
date = int(input())
weight = float(input())
lost_weight = (100 - 88) / 60
second_weight = 100 - (lost_weight * date)
if weight <= second_weight:
    print(f"Все идет по плану")
else:
    print(f"Что-то пошло не так")
print(f"#{date} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {second_weight:.2f} кг")


# ============================================================================
# ТЕМА 2: UNICODE И КОДЫ СИМВОЛОВ (Unicode & Character Codes)
# ============================================================================

# Задача №1 - Какая следующая буква? 
letter = input()
first_letter = ord("А")
last_letter = ord("Я")
if ord(letter) < last_letter:
    print(chr(ord(letter) + 1))
elif ord(letter) == last_letter:
    print("Дальше букв нет")

# Задача №2 - Символы в диапазоне
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=" ")

# Задача №3 - Простой шифр
text = input()
for i in range(len(text)):
    print(ord(text[i]), end=" ")

# Задача №4 - Самое тяжёлое слово 
largest = 0
largest_text = ""
for _ in range(4):
    text = input()
    total = 0
    for i in range(len(text)):
        total += ord(text[i])
    if total > largest:
        largest = total
        largest_text = text
print(largest_text)

# Задача №5 - Стоимость ответа 
text = input()
total = 0
for i in range(len(text)):
    total += (ord(text[i]) * 3)
print(f"Текст сообщения: '{text}'")
print(f"Стоимость сообщения: {total}🐝")

# Задача №6 - Накручиваем стоимость ответа ⬆️
text = input()
total = 0
for i in range(len(text)):
    total += (ord(text[i]) * 3)
print(f"Старая стоимость: {total}🐝")

eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"
text_2 = text

for i in range(len(eng)):
    text_2 = text_2.replace(eng[i], rus[i])
total_2 = 0
for z in range(len(text_2)):
    total_2 += (ord(text_2[z]) * 3)
print(f"Новая стоимость: {total_2}🐝")

# Задача №7 - Сбой в системе ️🌶️
text = input()
for i in range(64):
    text_right = ord("А") + i
    if str(text_right) in text:
        text = text.replace(f"[u-{text_right}]", chr(text_right))
print(text)

# Задача №8 - Шифр Цезаря 🌶️
num = int(input())
text = input()
new_text = ""
for i in range(len(text)):
    digit = ord(text[i]) - num
    if digit < 97:
        digit += 26
    new_text += chr(digit)
print(new_text)


# ============================================================================
# ТЕМА 3: СРАВНЕНИЕ СТРОК (String Comparison)
# ============================================================================

# Задача №1 - Волшебное число ✨
a, b, c, d = input(), input(), input(), input()
print((ord((min(a, b, c, d))[-1]) * ord((max(a, b, c, d))[-1])) ** 2)

# Задача №2 - Строковые минимум и максимум
text = input()
max_text = "A"
min_text = "яя"
while text != "КОНЕЦ":
    if text < min_text:
        min_text = text
    if text > max_text:
        max_text = text
    text = input()
print(f"Минимальная строка ⬇️: {min_text}")
print(f"Максимальная строка ⬆️: {max_text}")

# Задача №3 - Необычное сравнение 
text_1, text_2 = input(), input()
new_text_1 = ""
new_text_2 = ""
for i in range(len(text_1)):
    if text_1[i].isalpha():
        new_text_1 += text_1[i]
for j in range(len(text_2)):
    if text_2[j].isalpha():
        new_text_2 += text_2[j]

if new_text_1.lower() == new_text_2.lower():
    print("YES")
else:
    print("NO")

# Задача №4 - Сортируем слова 📶
a, b, c = input(), input(), input()
print(min(a, b, c), min(max(a, b), max(a, c), max(b, c)), max(a, b, c), sep=" ")

# Задача №5 - Название класса 👩‍🏫🌶️
n = int(input())
x = ord("А")
y = ord("П")
for _ in range(n):
    text = input()
    if len(text) == 2:
        if text[0] in "0123456789" and x <= ord(text[-1]) <= y:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

# Задача №6 - Порядок книг 📚🌶️
n = int(input())
flag = "YES"
prev_surname = ""
prev_title = ""
for _ in range(n):
    s = input()
    surname = s[:s.find(" ")]
    title = s[s.find("«") + 1 : s.find("»")]
    if surname < prev_surname:
        flag = "NO"
        break
    elif surname == prev_surname and title < prev_title:
        flag = "NO"
        break
    prev_surname = surname
    prev_title = title
print(flag)
