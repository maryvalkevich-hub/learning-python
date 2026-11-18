"""
Stepik: Python Programming
Topic: List Methods & String Processing
Date: 18 November 2026
Status: Completed ✅
Tasks solved: 6
Topics covered:
- List manipulation: append, extend, del, insert, sort, *=
- String methods: split(), join(), count(), rstrip(), find()
- Sorting with custom keys: sort(key=int)
- Tuple unpacking for variable swapping
Notable achievements:
- Task #3: Handled edge cases with trailing spaces using .rstrip()
- Task #4: Correctly compared string-numbers by casting to int inside the loop
- Task #5: Applied key=int for proper numeric sorting of string lists
Personal note: Solid understanding of list mechanics and string processing. 
Ready for the next topic.
"""

  # Задача №1 - Количество артиклей
  # На вход программе подаётся строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей a, an, the и выводит текст в следующем формате:
  # Общее количество артиклей: <total>
  # Примечание. Артикли могут начинаться с заглавной буквы A, An, The.
text = input().lower().split()
total = text.count('a') + text.count('an') + text.count('the')
print(f"Общее количество артиклей: {total}")

  # Задача №2 - Всё сразу 2
  # Дополните приведённый ниже код, чтобы он:
  # Заменил второй (по порядку) элемент списка на 17;
  # Добавил числа 4, 5 и 6 в конец списка;
  # Удалил первый (по порядку) элемент списка;
  # Удвоил список;
  # Вставил число 25 по индексу 3;
  # Вывел список с помощью функции print()
  # Примечание. Под удвоением списка мы понимаем добавление к исходному списку всех его элементов, сохраняя порядок. Например, при удвоении списка ['py', 'gen'] мы получаем список ['py', 'gen', 'py', 'gen'].
  # код - numbers = [8, 9, 10, 11]
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)

  # Задача №3 - Взлом Братства Стали
  # Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали и любезно соглашается помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не оставляют комментарии к коду и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.
  # Примечание 1. Обращайте внимание на лишние пробелы в конце строк. Проверяющая система не пропустит ваше решение с ними.
  # Примечание 2. Гарантируется, что в самом коде программы отсутствуют символы #.
a = input()
b = int(a[1:])
for _ in range(b):
    texts = input()
    if "#" in texts:
        x = texts.find("#")
        texts = texts[:x]
        print(texts.rstrip())
    else:
        print(texts.rstrip())

  # Задача №4 - Переставить min и max 🌶️
  # На вход программе подаётся строка текста, содержащая различные натуральные числа. Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.
  # Примечание. Используйте подходящие встроенные функции и списочные методы.
numbers = input().split()
max_idx = 0
min_idx = 0
for i in range(len(numbers)):
    if int(numbers[i]) > int(numbers[max_idx]):
        max_idx = i
    if int(numbers[i]) < int(numbers[min_idx]):
        min_idx = i
numbers[max_idx], numbers[min_idx] = numbers[min_idx], numbers[max_idx]

print(" ".join(numbers))

  # Задача №5 - Сортировка чисел
  # На вход программе подаётся строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
numbers = input().split()
numbers.sort(key=int)
print(*numbers)
numbers.sort(key=int, reverse=True)
print(*numbers)

  # Задача №6 - Сортируем песни 🎵
  # На вход программе подаются число n, а затем – n песен из плейлиста Сэма, каждая на отдельной строке. Напишите программу, которая сортирует эти песни в алфавитном порядке и выводит каждую из них на отдельной строке.
n = int(input())
songs = []
for _ in range(n):
    text = input()
    songs.append(text)
songs.sort()
print(*songs, sep = "\n")
