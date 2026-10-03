"""
Stepik Exam: String Operations (Completed ✅)
Date: 20 September 2026
Result: Passed with confidence! 

This file contains all tasks from the Strings module exam.
Notable solutions:
- Task 10: Creative use of replace("f", "_", 1) to find the second occurrence.
- Task 11: Elegant slice concatenation for reversing a substring between two characters.
"""

# Задача №1 - Длина строки
s = 'Python rocks!'
print(len(s))

# Задача №2 - Четвертый символ
s = 'Python rocks!'
print(s[3])

# Задача №3 - Срез со 2-го по 5-й включительно
s = 'Python rocks!'
print(s[1:5])

# Задача №4 - Удаление замыкающих символов '#'
s = '###Python rocks!####'
print(s.strip("#"))

# Задача №5 - Верхний регистр
s = 'Python rocks!'
print(s.upper())    

# Задача №6 - Замена символов
s = 'Python rocks!'
print(s.replace("o", "@"))

# Задача №7 - Каждый третий (удаление символов с индексами, кратными 3)
text = input()
total = ""
for i in range(len(text)):
    if i % 3 != 0:
        total += text[i]
print(total)

# Задача №8 - Замени меня полностью
text = input()
print(text.replace("1", "one"))

# Задача №9 - Удали меня полностью
text = input()
print(text.replace("@", ""))

# Задача №10 - Второе вхождение 'f' (Креативное решение!)
text = input()
counter_f = 0
for i in range(len(text)):
    if text[i] == "f":
        counter_f += 1

if counter_f >= 2:
    # Гениальный хак: заменяем только первую 'f' на '_', чтобы найти вторую
    new_text = text.replace("f", "_", 1)
    print(new_text.find("f"))
elif counter_f == 1:
    print("-1")
else:
    print("-2")

# Задача №11 - Переворот между первым и последним 'h'
text = input()
text_1 = text[text.find("h") + 1 : text.rfind("h")]
print((text[:text.find("h") + 1]) + (text_1[::-1]) + (text[text.rfind("h"):]))
