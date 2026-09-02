"""
Stepik: Python Programming
Topic: Strings (Строки), Indexing, and Basic Iteration
Date: 29 August 2026
Status: Completed ✅

Tasks solved: 12 (Indexing, Reverse iteration, Initials, Emoji queue, Digit sum, Neighbor check, Vowels/Consonants, Decimal to Binary)
Topics covered:
- Positive and negative indexing (e.g., s[-10]).
- Iterating through strings with step (range(0, len, 2)).
- String formatting (f-strings).
- Character classification (checking membership in "0123456789" or vowel strings).
- Manual binary conversion algorithm using while loops and string concatenation.

Notable achievements:
- Successfully implemented boundary-safe neighbor comparison (Task 10) avoiding IndexError.
- Mastered the manual decimal-to-binary conversion algorithm, correctly handling string concatenation order and loop termination.
- Demonstrated flexibility by solving digit-sum problems using both mathematical (modulo) and string-iteration approaches.

Personal note: Completed this module while recovering from a migraine and managing family logistics. Proof that consistent, gentle pacing yields solid results.
"""

  # Задача №1 - Используя индексатор, дополните приведённый ниже код так, чтобы он вывел символ запятой.
  # Код задача:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])  # мой ответ 7. В условии задачи в скобках пропуск


  # Задача №2 - Используя индексатор, дополните приведённый ниже код так, чтобы он вывел символ w.
  # Код задачи:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])  # мой ответ -10.

  # Задача №3 - В столбик 1
  # На вход программе подаётся одна строка. Напишите программу, которая выводит элементы строки с чётными индексами (0, 2, 4, ...).
text = input()
for i in range(0, len(text), 2):
    print(text[i])

  # Задача №4 - В столбик 2
  # На вход программе подаётся одна строка. Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
text = input()
for i in range(1, (len(text) + 1)):
    print(text[-i])

  # Задача №5 - ФИО
  # На вход программе подаются три строки: имя, фамилия и отчество (именно в таком порядке). Напишите программу, которая выводит инициалы человека.
  # Примечание. Гарантируется, что имя, фамилия и отчество начинаются с заглавной буквы.
name = input()
surname = input()
second_name = input()
print(surname[0], name[0], second_name[0], sep = "")

  # Задача №6 - По одному ☝️
  # Персонажи мультфильма «Мадагаскар» планируют побег из Африки. Они выстроились в очередь на самолёт, построенный шимпанзе.
  # На вход программе подаётся строка из эмодзи-символов – очередь животных на борт самолёта. Для каждого животного из очереди вам необходимо вывести его эмодзи и номер в очереди (начиная с 1) в следующем формате:
  # <номер животного в очереди>) <эмодзи животного>
text = input()
for i in range(0, len(text)):
    print(f"{i + 1}) {text[i]}")

  # Задача №7 - Цифра 1
  # На вход программе подаётся одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
  # Вариант 1 - какое решение сразу пришло в голову.
num = int(input())
total = 0
while num != 0:
    digit = num % 10
    total += digit
    num //= 10
print(total)

  # Вариант 2 - если по теме лекции(Строки).
num = input()
total = 0
for i in range(0, len(num)):
    total += int(num[i])
print(total)

  # Задача №8 - Цифра 2.
  # На вход программе подаётся одна строка. Напишите программу, которая выводит сообщение «Цифра» (без кавычек), если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).
text = input()
counter = 0
for i in range(len(text)):
    if text[i] in "0123456789":
        counter += 1
        
if counter > 0:
    print("Цифра")
     
else:
    print("Цифр нет")
    

  # Задача №9 - Сколько раз?
  # На вход программе подаётся одна строка. Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *, и выводит текст в следующем формате:
  # Символ + встречается <n> раз
  # Символ * встречается <m> раз
  # где <n>, <m> – количество вхождений символов + и * в строку соответственно.
text = input()
counter1 = 0
counter2 = 0
for i in range(len(text)):
    if text[i] in "+":
        counter1 += 1
    if text[i] in "*":
        counter2 += 1
print(f"Символ + встречается {counter1} раз")
print(f"Символ * встречается {counter2} раз")


  # Задача №10 - Одинаковые соседи
  # На вход программе подаётся одна строка. Напишите программу, которая определяет, сколько в ней пар одинаковых соседних символов.
text = input()
counter = 0
for i in range(len(text) - 1):
     if text[i] == text[i + 1]:
          counter += 1
print(counter)

  # Задача №11 - Гласные и согласные 🔠
  # На вход программе подаётся одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
  # Количество гласных букв равно <кол-во гласных букв>
  # Количество согласных букв равно <кол-во согласных букв>
  # Примечание. Ваша программа должна игнорировать все небуквенные символы, а также букву ё.
text = input()
counter1 = 0
counter2 = 0
for i in range(len(text)):
        if text[i] in "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
                counter2 += 1
        if text[i] in "ауоыиэяюёеАУОЫИЭЯЮЁЕ":
                counter1 += 1
    
print(f"Количество гласных букв равно {counter1}")
print(f"Количество согласных букв равно {counter2}")

  # Задача №12 - Decimal to Binary 🔟🌶️
  # На вход программе подаётся натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
n = int(input())
b = ""
while n != 0:
     x = n % 2
     b = str(x) + b
     n //= 2
print(b)
