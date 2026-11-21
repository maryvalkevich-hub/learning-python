"""
Stepik Tasks — List Comprehensions (Списочные выражения)
Date: 08 November 2026
Topics: list comprehensions, conditional filtering, string methods in lists, 
        mathematical checks (palindromes), unpacking (*)
Result: 9 tasks completed
Notable achievements:
- Task 4: Elegant mathematical check for 3-digit palindromes (i % 10 == i // 100).
- Task 6 & 7: Clean use of unpacking (*) with list comprehensions for formatted output.
- Task 9: Complex conditional filtering (even numbers, excluding squares ending in 4).
Personal note: Mastered the transition from traditional for-loops to concise, Pythonic list comprehensions.
"""


  # Задача №1 - Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список, содержащий строки исходного списка, где у каждой строки удалён первый символ.
  # Код:
  # keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
  # new_keywords = 
  # print(new_keywords)
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1:] for m in keywords]
print(new_keywords)

  # Задача №2 - Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список, содержащий длины строк исходного списка.
  # код:
  # keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
  # lengths = 
  # print(lengths)
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

  # Задача №3 - Используя списочное выражение, дополните приведённый ниже код так, чтобы получить новый список, содержащий только слова длиной не менее пяти символов (включительно).
  # код:
  # keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
  # new_keywords =
  # print(new_keywords)
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m for m in keywords if len(m) >= 5]
print(new_keywords)

  # Задача №4 - Используя списочное выражение, дополните приведённый ниже код так, чтобы получить список всех целых чисел-палиндромов от 100 до 1000 (включительно) в порядке возрастания.
  # palindromes = 
  # print(palindromes)
palindromes = [i for i in range(100, 1001) if i % 10 == i // 100]
print(palindromes)

  # Задача №5 - В одну строку 1
  # На вход программе подаётся строка текста, содержащая слова. Напишите программу, которая выводит слова введённой строки в столбик.
  # Примечание. Программу можно написать в одну строку кода.
print(*(input().split()), sep = "\n")

  # Задача №6 - Списочное выражение 1
  # На вход программе подаётся натуральное число n. Напишите программу, использующую списочное выражение, которая создаёт список, содержащий квадраты чисел от 1 до n (включительно), а затем выводит его элементы построчно, то есть каждый на отдельной строке.
  # Примечание. Для вывода элементов списка используйте цикл for.
print(*[i**2 for i in range(1, int(input()) + 1)], sep = '\n')

  # Задача №7 - Списочное выражение 2
  # На вход программе подаётся строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет кубы указанных чисел на одной строке.
  # Примечание 1. Для вывода элементов списка используйте цикл for.
  # Примечание 2. Используйте метод split().
print(*[int(i) ** 3 for i in input().split()])

  # Задача №8 - В одну строку 2
  # На вход программе подаётся строка текста. Напишите программу, использующую списочное выражение, которая выводит все цифровые символы данной строки.
print(*[i for i in input() if i.isdigit()], sep = "")

  # Задача №9 = В одну строку 3
  # На вход программе подаётся строка текста, содержащая целые числа. Напишите программу, использующую списочное выражение, которая выведет квадраты чётных чисел, кроме тех квадратов, которые оканчиваются на цифру 4.
print(*[int(i)**2 for i in input().split() if (int(i) % 2 == 0) and (int(i) ** 2) % 10 != 4])
