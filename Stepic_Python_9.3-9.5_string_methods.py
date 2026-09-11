"""
Stepik: Python Programming
Topic: String Methods (Методы строк) — Complete Module
Date: 10 September 2026
Status: Completed ✅

Subtopics covered:
1. Case Conversion Methods (Методы конвертации регистра)
2. Search & Replace Methods (Методы поиска и замены)
3. Character Classification Methods (Методы классификации символов)

Tasks solved: 15 total
- Case Conversion: 4 tasks (title check, swapcase, case-insensitive substring search, lowercase counter)
- Search & Replace: 8 tasks (word count, DNA code analysis, Morse code validation, digit counter, domain check, most frequent char, first/last occurrence, fragment removal)
- Character Classification: 3 tasks (comment validation, nickname validation, license plate validation)

Topics covered:
- Case conversion: .title(), .swapcase(), .lower(), .upper(), .capitalize()
- Search & replace: .count(), .find(), .rfind(), .startswith(), .endswith(), .replace()
- Character classification: .isspace(), .isalnum(), .isdigit(), .isupper(), .islower()
- String slicing combined with methods for complex validation
- Edge case handling: empty strings, whitespace-only strings, odd/even length splits

Notable achievements:
- Mastered case-insensitive substring search using .lower() before .count() or 'in' check.
- Learned to distinguish between checking a single character (text[i].isdigit()) vs. a substring (text[1:4].isdigit()).
- Successfully combined multiple string methods in complex validation tasks (nickname format, license plate format).
- Applied .strip() concept for whitespace-only string detection.
- Demonstrated progressive problem-solving: from brute-force loops to elegant one-liners using built-in methods.

Personal note: Completed this module during a busy week with a toddler, migraines, and household chaos. Proved that consistent, gentle pacing + good rest = deep understanding. The "read → rest → consolidate" learning rhythm is working beautifully.
"""
  # Case Conversion Methods (Методы конвертации регистра)
  # Задача №1 - Заглавные буквы 🔠
  # На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
  # Примечание. Строка содержит только буквы и символ пробела.
text = input()
s = text.title()
if text == s:
    print("YES")
else:
    print("NO")

  # Задача №2 - sWAP cASE 🔃
  # На вход программе подаётся строка. Напишите программу, которая меняет регистр символов – заменяет все строчные символы заглавными и наоборот.
text = input()
print(text.swapcase())

  # Задача №3 - Хороший оттенок 👍
  # На вход программе подаётся строка текста. Напишите программу, которая определяет, является ли оттенок текста хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» (без кавычек) во всевозможных регистрах.
  # Примечание. Текст, содержащий «хорош», «ХОРОШ», «Хорош», «хОРОШ» и так далее также имеет хороший оттенок.
text = input()
s = text.lower()
if "хорош" in s:
    print("YES")
else:
    print("NO")

  # Задача №4 - Нижний регистр 🔽
  # На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
  # Вариант 1 - то, что первым пришло в голову.
text = input()
counter = 0
for i in range(len(text)):
    if text[i] in "abcdefghijklmnopqrstuvwxyz":
        counter += 1
print(counter)

  # Вариант 2 - если по теме лекции.
text = input()
counter = 0
for i in text:
    if i != i.upper():
        counter += 1
print(counter)

  # Search & Replace Methods (Методы поиска и замены)
  # Задача №1 - Количество слов.
  # На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.
  # Примечание. Строка текста не содержит пробелов в начале и конце.
text = input()
counter = text.count(" ")
print(counter + 1)  # Так как нет пробелов по стороном предложения, то можно просто посчитать количество пробелов внутри и прибавить 1.

  # Задача №2 - Минутка генетики 🧬
  # На вход программе подаётся строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин) и Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
  # Примечание. Строка не содержит других символов, кроме А, Г, Ц, Т, а, г, ц, т.
  # Вариант 1 - что первым пришло в голову
text = input()
counter_a = 0
counter_g = 0
counter_t = 0
counter_c = 0
for i in range(len(text)):
    if text[i] in "аА":
        counter_a += 1
    if text[i] in "Гг":
        counter_g += 1
    if text[i] in "Тт":
        counter_t += 1
    if text[i] in "Цц":
        counter_c += 1
print(f"Аденин: {counter_a}")
print(f"Гуанин: {counter_g}")
print(f"Цитозин: {counter_c}")
print(f"Тимин: {counter_t}")

  # Вариант 2 - с учетом темы лекции по методам поиска и замены.
text = input().lower()
counter_a = text.count('а')
counter_g = text.count('г')
counter_t = text.count("т")
counter_c = text.count('ц')
print(f"Аденин: {counter_a}")
print(f"Гуанин: {counter_g}")
print(f"Цитозин: {counter_c}")
print(f"Тимин: {counter_t}")

  # Задача №3 - Очень странные дела 📻
  # Джим Хоппер с помощью радиоприёмника пытается получить сообщение Оди. На приёмник ему поступает n различных последовательностей кода Морзе. Декодировав их, он получает последовательности из цифр и букв строчного латинского алфавита. При этом только в сообщениях Оди содержится число 
  # 11, причём минимум 3 раза. Помогите определить Джиму количество сообщений от Оди.
  # Примечание. Обратите внимание, что в сообщениях Оди вхождения числа 11 должны быть непересекающимися. Другими словами, если мы нашли вхождение числа 11, то следующее вхождение должно начинаться строго после окончания предыдущего. Например, в строке '111' содержится одна такая последовательность, в то время как в '1111' их уже две.
n = int(input())
counter = 0
for _ in range(n):
    text = input()
    if text.count("11") >= 3:
        counter += 1
print(counter)

  # Задача №4 - Количество цифр
  # На вход программе подаётся строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
  # Вариант 1 - что пришло сразу в голову.
text = input()
counter = 0
for i in range(len(text)):
    if text[i] in "0123456789":
        counter += 1
print(counter)

  # Вариант 2 - по теме лекции по методам поиска и замены.ы
text = input()
counter = 0
for i in range(10):
    counter += text.count(str(i))
print(counter)

  # Задача №5 - .com or .ru 🌐
  # На вход программе подаётся строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
  # Программа должна вывести «YES» (без кавычек), если введённая строка заканчивается подстрокой .com или .ru, или «NO» (без кавычек) в противном случае.
text = input()
flag = "NO"
if text.endswith(".com") or text.endswith(".ru"):
    flag = "YES"
print(flag)  

  # Задача №6 - Самый частотный символ
  # На вход программе подаётся строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
  # Примечание 1. Если таких символов несколько, следует вывести последний по порядку символ.
  # Примечание 2. Следует различать заглавные и строчные буквы, а также буквы русского и английского алфавита.
text = input()
x = 0
y = ""
for i in range(len(text)):
    if text.count(text[i]) >= x:
        x = text.count(text[i])
        y = text[i]
print(y)

  # Задача № 7 - Первое и последнее вхождение
  # На вход программе подаётся строка текста. Если в этой строке буква «f» встречается только один раз, выведите её индекс. Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной строке, разделённые символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO» (без кавычек).
text = input()
counter = text.count("f")   # я бы еще привела все символы к нижнему регистру, мало ли есть символ f в верхнем регистре, но по усливию задачи это не нужно
if counter == 1:
    print(text.find("f"))
elif counter >= 2:
    print(text.find("f"), text.rfind("f"))
else:
    print("NO")

  # Задача №8 - Удаление фрагмента
  # На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза. Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h», а также все символы, находящиеся между ними.
text = input()
x = text.find("h")
y = text.rfind("h")
print(text[:x], text[(y + 1):], sep = "")


  # Character Classification Methods (Методы классификации символов)
  # Задача №1 - Плохие комментарии 😈
  # На платформе Stepik пользователи оставляют комментарии, но не все из них соответствуют правилам. Так, например, модератор Сэм считает неуместными комментариями те, которые представляют собой пустую строку или состоят только из пробелов. Подобные комментарии он удаляет – нечего засорять курс бесполезным материалом!
  # Ваша задача – написать программу, которая поможет Сэму проверять комментарии. Программа должна принимать на вход натуральное число n, а затем n строк, представляющих тексты комментариев. Для каждого комментария ваша программа должна выводить номер этого комментария (начиная с 1), затем двоеточие (:), затем через пробел его текст или сообщение «COMMENT SHOULD BE DELETED» (без кавычек), если комментарий должен быть удалён Сэмом.
n = int(input())
for i in range(n):
    text = input()
    if len(text) == 0 or text.isspace():
        print(f"{i + 1}: COMMENT SHOULD BE DELETED")
    else:
        print(f"{i + 1}: {text}")

  # Задача №2 - Проверь никнейм 👩🌶️
  # Во время собеседования вам предложили решить задачу на валидацию имени пользователя. Пользователь пытается создать никнейм для своего аккаунта в соцсети Y. Правила для корректного никнейма в соцсети Y следующие:
  # никнейм должен начинаться с символа @
  # никнейм должен содержать от 5 до 15 (включительно) символов (включая первый символ @)
  # никнейм должен содержать только строчные буквы и (или) цифры (помимо первого символа @)
  # Напишите программу, которая выводит «Correct» (без кавычек), если никнейм соответствует всем вышеприведенным правилам, или «Incorrect» (без кавычек) в противном случае.
  # Примечание. Обратите внимание, что никнейму необязательно содержать строчные буквы и цифры одновременно, никнейм может содержать только строчные буквы или только цифры (помимо первого символа @).
text = input()
text_2 = text[1:]
text_3 = text.lower()
if text.startswith("@") and 5 <= len(text) <= 15 and text_2.isalnum() and text_3 == text:
    print("Correct")
else:
    print("Incorrect")

  # Задача №3 - Автомобильный номер 🚘🌶️
  # В службе по дорожному движению решили оптимизировать процесс создания автомобильных номеров: вместо человека генерацию автомобильных номеров поручили некоторой GPT (модели машинного обучения). Как мы знаем, искусственный интеллект ещё сыроват и делает много ошибок, поэтому его результаты следует тщательно проверять. Корректный автомобильный номер (в России) имеет следующий формат:
  # C065MK 78 rus
  # Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером. Программа должна вывести «YES» (без кавычек), если искусственный интеллект справился со своей задачей, или «NO» (без кавычек) в противном случае. В нашей задаче корректным автомобильным номером будем считать следующие форматы:
  # <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
  # <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
  # где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы АВЕКМНОРСТУХ.
text = input()
letters = "АВЕКМНОРСТУХ"

if len(text) in [9, 10]:
    if (text[0] in letters and text[0].isupper() and
        text[1:4].isdigit() and
        text[4] in letters and text[4].isupper() and
        text[5] in letters and text[5].isupper() and
        text[6] == "_" and
        text[7:].isdigit()):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

