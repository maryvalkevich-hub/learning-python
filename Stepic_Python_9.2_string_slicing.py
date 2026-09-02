"""
Stepik: Python Programming
Topic: String Slicing (Срезы) and Advanced Indexing
Date: 02 September 2026
Status: Completed ✅

Tasks solved: 8 (Basic slicing, Reverse slicing, Palindrome check, Complex multi-slice operations, String splitting/swapping)
Topics covered:
- Basic slicing syntax: `[start:stop]`, `[:stop]`, `[start:]`.
- Step parameter in slicing: `[::step]`, `[start:stop:step]`.
- Negative indexing in slices: `[-9:]`, `[:-2]`.
- String reversal using `[::-1]` and `[::-2]`.
- Extracting even/odd indexed characters using `[0::2]` and `[1::2]`.
- Algorithmic string manipulation: splitting a string in half and swapping parts (handling odd/even lengths).

Notable achievements:
- Successfully optimized palindrome checking from a `while` loop approach to a clean, Pythonic one-liner using `[::-1]`.
- Mastered complex slicing combinations to extract specific character patterns (e.g., removing first and last characters via `[1:-1]`).
- Demonstrated strong logical thinking in Task 8 by correctly handling the edge case of odd-length strings during the split-and-swap operation.

Personal note: Adopted a new, highly effective learning rhythm (read -> rest -> consolidate via notes). Proving that gentle pacing and listening to one's body leads to deeper understanding and better retention.
"""

  # Задача №1 - Используя срезы, дополните приведённый ниже код так, чтобы он вывел первые 12 символов строки s.
  # код задания:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print()

  # мой код:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

  # Задача №2 - Используя срезы, дополните приведённый ниже код так, чтобы он вывел последние 9 символов строки s.
  # код задачи
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print()

  # мой код:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

  # Задача №3 - Используя срезы, дополните приведённый ниже код так, чтобы он вывел каждый 7 символ строки s (начиная с 0-го индекса).
  # код задачи
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print()

  # мой код:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

  # Задача №4 - Используя срезы, дополните приведённый ниже код так, чтобы он вывел строку s в обратном порядке.
  # код задачи:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print()

  # мой код:
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

  # Задача №5 - На вход программе подаётся одно слово, записанное в нижнем регистре. Напишите программу, которая определяет, является ли оно палиндромом.
  # Программа должна вывести «YES» (без кавычек), если слово является палиндромом, или «NO» (без кавычек) в противном случае.
text = input()
text2 = text[::-1]
if text == text2:
    print("YES")
else:
    print("NO")

  # Задача №6 - Делаем срезы 1
  # На вход программе подаётся одна строка. Напишите программу, которая выводит:
  # общее количество символов в строке;
  # исходную строку, повторённую 3 раза;
  # первый символ строки;
  # первые три символа строки;
  # последние три символа строки;
  # строку в обратном порядке;
  # строку с удалённым первым и последним символами.
text = input()
print(len(text), text[:] * 3, text[0:1], text[0:3], text[-3:], text[::-1], text[1:][:-1], sep = "\n")

  # Задача №7 - Делаем срезы 2
  # На вход программе подаётся одна строка. Напишите программу, которая выводит:
  # третий символ этой строки;
  # предпоследний символ этой строки;
  # первые пять символов этой строки;
  # всю строку, кроме последних двух символов;
  # все символы с чётными индексами;
  # все символы с нечётными индексами;
  # все символы в обратном порядке;
  # все символы строки через один в обратном порядке, начиная с последнего.
text = input()
print(text[2], text[-2], text[0:5], text[:-2], text[0::2], text[1::2], text[::-1], text[::-2], sep = "\n")

  # Задача №8 - Две половинки 🌶️.
  # На вход программе подаётся строка текста. Напишите программу, которая разрежет её на две равные части, переставит их местами и выведет на экран.
  # Примечание. Если длина строки нечётная, то длина первой части должна быть на один символ больше.
text = input()
x = len(text)
if x % 2 == 0:
    print(text[(x // 2):], text[0:(x // 2)], sep = "")
elif x % 2 != 0:
    print(text[(x // 2) + 1:], text[0:(x // 2) + 1], sep = "")
