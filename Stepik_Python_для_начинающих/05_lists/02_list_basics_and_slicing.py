"""
Stepik Tasks — List Basics & Slicing (Основы работы со списками)
Date: 04 November 2026
Topics: indexing, slicing, list length, del operator, min/max
Result: 4 tasks completed
"""

# Задача №1 - Используя индексатор, дополните приведённый ниже код так, чтобы он вывел 17-ый (по порядку) элемент списка primes.
  # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
  # print()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])

  # Задача №2 - Используя индексатор, дополните приведённый ниже код так, чтобы он вывел последний элемент списка primes.
  # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
  # print()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])

  # Задача №3 - Используя срезы, дополните приведённый ниже код так, чтобы он вывел первые 6 элементов списка primes.
  # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
  # print()
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])

  # Задача №4 - Дополните приведённый ниже код так, чтобы он вывел сумму минимального и максимального элементов списка numbers.
  # numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
  # print()
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(max(numbers) + min(numbers))

  # Задача №5 - Дополните приведённый ниже код так, чтобы он вывел среднее арифметическое элементов списка evens.
  # evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  # average = 
  # print(average)
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)

  # Задача №6 - Дополните приведённый ниже код так, чтобы элемент списка имеющий значение Green заменился на значение Зеленый, а элемент Violet – на Фиолетовый. Далее необходимо вывести полученный список.
  # rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
  # print()
  # Вариант 1 - это когда мы видем список и четко знаем индексы того, что нужно заменить
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'

print(rainbow)

  # Вариант 2 - когда мы не видем весь список и нам нужно сначала найти, а потом заменить.
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
for i in range(len(rainbow)):
    if rainbow[i] == 'Green':
        rainbow[i] = 'Зеленый'
    if rainbow[i] == 'Violet':
        rainbow[i] = 'Фиолетовый'

print(rainbow)

  # Задача №7 - Дополните приведённый ниже код так, чтобы он вывел "перевёрнутый" список languages (то есть элементы будут идти в обратном порядке).
  # languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
new_languages = languages[::-1]
print(new_languages)

  # Задача №8 - Используя операторы конкатенации (+) и умножения списка на число (*), дополните приведённый ниже код так, чтобы он вывел следующий список:
  # [1, 2, 3, 1, 2, 3, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13]
  # numbers1 = [1, 2, 3]
  # numbers2 = [6]
  # numbers3 = [7, 8, 9, 10, 11, 12, 13]
  # print()
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print((numbers1 * 2) + (numbers2 * 9) + numbers3)
