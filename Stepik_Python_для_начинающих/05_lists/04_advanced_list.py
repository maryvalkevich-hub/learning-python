"""
Stepik Tasks — Advanced List Operations (Продвинутые операции со списками)
Date: 06 November 2026
Topics: list comprehensions, unpacking (*), string methods (.lower()), 
        del with index(), conditional filtering, nested loops
Result: 7 tasks completed (6/7 correct on first attempt)
"""

  # Задача №1 - Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.
  # numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
total = 0
for num in numbers:
    total += (num ** 2)
print(total)

  # Задача №2 - Negatives, Zeros and Positives
  # На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа. Все числа должны быть выведены в том же порядке, в котором они были введены, каждое на отдельной строке.
n = int(input())
numbers1 = []
numbers2 = []
numbers3 = []
for _ in range(n):
    digit = int(input())
    if digit > 0:
        numbers1.append(digit)
    if digit == 0:
        numbers2.append(digit)
    if digit < 0:
        numbers3.append(digit)
    
print(*numbers3, *numbers2, *numbers1, sep = "\n")

  # Задача №3 - Без дубликатов
  # На вход программе подаются натуральное число n, а затем n строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.
  # Примечание. Считайте, что все строки состоят из строчных символов.
n = int(input())
words = []
for _ in range(n):
    text = input()
    if text not in words:
        words.append(text)
print(*words, sep = "\n")

  # Задача №4 - Значение функции
  # На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого введённого числа x выводит значение функции f(x)=x^2+2x+1, каждое на отдельной строке.
  # Примечание. Для первого теста имеем:
  # f(1)=1^2+2⋅1+1=4,f(2)=2^2+2⋅2+1=9,f(3)=3^2+2⋅3+1=16,…
n = int(input())
for _ in range(n):
    digit = int(input())
    x = (digit ** 2) + (2 * digit) + 1
    print(x)

  # Задача №5 - Remove outliers
  # При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и самое маленькое значение. 
  # На вход программе подаются натуральное число n, а затем n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.
n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
del numbers[numbers.index(max(numbers))]
del numbers[numbers.index(min(numbers))]
print(*numbers, sep = "\n")

  # Задача №6 - Google search - 1
  # На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка – поисковый запрос. Напишите программу, которая выводит все введённые строки, в которых встречается поисковый запрос.
  # Примечание. Поиск не должен быть чувствителен к регистру символов.
n = int(input())
texts = []
for _ in range(n):
    texts.append(input())
word = input()
for i in texts:
    if word.lower() in i.lower():
        print(i)

  # Задача №7 - Google search - 2
  # На вход программе подаются натуральное число n, затем n строк, затем число k – количество поисковых запросов, затем k строк – поисковые запросы. Напишите программу, которая выводит все введённые строки, в которых встречаются одновременно все поисковые запросы.
  # Примечание. Поиск не должен быть чувствителен к регистру символов.
n = int(input())
texts = []
texts2 = []
texts3 = []
for _ in range(n):
    texts.append(input())
number = int(input())
for _ in range(number):
    texts2.append(input())
for i in range(len(texts)):
    counter = 0
    for j in range(len(texts2)):
        if texts2[j].lower() in texts[i].lower():
            counter += 1
    if counter == number:
        texts3.append(texts[i])
print(*texts3, sep = "\n")
