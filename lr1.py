# 1. Числа и арифметика
import math
a = 10
b = 3.5
print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)
print("Деление:", a / b)
print("Тип результата деления:", type(a / b))
radius = 5
area = math.pi * radius ** 2
rounded_area = round(area, 2)
print(f"Площадь круга с радиусом {radius}: {rounded_area}")
print("\n" + "="*50 + "\n")

# 2. Работа со строками
text = " Hello, Python! "
result = text.strip().replace('!', '?').upper()
print("Результат цепочки операций:", result)
cleaned_text = text.strip().lower()
print("Очищенный текст:", cleaned_text)
assert cleaned_text == "hello, python!", "Строка не соответствует ожидаемому результату"
print("Проверка assert пройдена успешно")
print("\n" + "="*50 + "\n")

# 3. Списки
numbers = [7, 2, 5]
numbers.append(4)
print("После append(4):", numbers)
numbers.insert(1, 10)
print("После insert(1, 10):", numbers)
numbers.extend([1, 1, 1])
print("После extend([1, 1, 1]):", numbers)
numbers.remove(7)
print("После remove(7):", numbers)
last_element = numbers.pop()
print("После pop(), удаленный элемент:", last_element)
print("Список после pop():", numbers)
numbers.sort()
print("После sort():", numbers)
numbers.reverse()
print("После reverse():", numbers)
count_2 = numbers.count(2)
print("Количество вхождений числа 2:", count_2)
index_1 = numbers.index(1)
print("Индекс первого вхождения числа 1:", index_1)
copy_list = numbers.copy()
import copy
deepcopy_list = copy.deepcopy(numbers)
numbers.clear()
print("Исходный список после clear():", numbers)
print("Копия через copy():", copy_list)
print("Копия через deepcopy():", deepcopy_list)
print("\n" + "="*50 + "\n")

# 4. Кортежи
t = (1, 2, 3)
try:
    t[1] = 100
except TypeError as e:
    print(f"Ошибка при попытке изменить кортеж: {e}")
t2 = t + (4, 5)
print("Объединенный кортеж t2:", t2)
count_3 = t2.count(3)
print("Количество вхождений числа 3 в t2:", count_3)
index_4 = t2.index(4)
print("Индекс числа 4 в t2:", index_4)
print("Исходный кортеж t остался неизменным:", t)
print("\n" + "="*50 + "\n")

# 5. Множества
values = [3, 1, 3, 2, 1, 5, 2]
unique_values = set(values)
print("Исходный список:", values)
print("Множество unique_values:", unique_values)
print("Количество уникальных элементов:", len(unique_values))
other = {2, 4, 5}
print("Второе множество other:", other)
print("Пересечение множеств:", unique_values & other)
print("Объединение множеств:", unique_values | other)
print("Разность unique_values - other:", unique_values - other)
print("Разность other - unique_values:", other - unique_values)
print("\n" + "="*50 + "\n")

# 6. Словари
scores = {"Alice": 85, "Bob": 90}
print("Исходный словарь:", scores)
scores["Charlie"] = 78
print("После добавления Charlie:", scores)
scores["Bob"] = 95
print("После обновления Bob:", scores)
dave_score = scores.get("Dave", "не найден")
bob_score = scores.get("Bob", "не найден")
print("Балл Dave:", dave_score)
print("Балл Bob:", bob_score)
scores.pop("Alice")
print("После удаления Alice:", scores)
print("Количество записей в словаре:", len(scores))
assert "Alice" not in scores, "Alice все еще в словаре"
print("Ключи словаря:", list(scores.keys()))
print("Значения словаря:", list(scores.values()))
print("\n" + "="*50 + "\n")

# 7. Комбинированное задание
text = """
Python is a powerful programming language.
It is used in data science, web development, automation, and many other fields!
PYTHON is easy to learn, yet very versatile.
"""
cleaned_text = text.strip().lower().replace('!', '.')
print("Очищенный текст:")
print(cleaned_text)
sentences = [s.strip() for s in cleaned_text.split('.') if s.strip()]
print("\nСписок предложений:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")
first_sentence = sentences[0]
print(f"\nПервое предложение: {first_sentence}")
words = first_sentence.split()
print("Слова первого предложения:", words)
python_count = first_sentence.count("python")
print(f"Количество 'python' в первом предложении: {python_count}")
starts_with_python = first_sentence.startswith("python")
ends_with_language = first_sentence.endswith("language")
print(f"Начинается с 'python': {starts_with_python}")
print(f"Заканчивается на 'language': {ends_with_language}")
total_chars = len(first_sentence)
count_a = first_sentence.count("a")
data_index = first_sentence.find("data")
print(f"Общее количество символов: {total_chars}")
print(f"Количество букв 'a': {count_a}")
print(f"Индекс слова 'data': {data_index}")
joined_words = "-".join(words)
print(f"Слова, соединенные через '-': {joined_words}")
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
print("Словарь частот слов:", word_freq)
def clean_text(text):
    import string
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())
    return text
test_text = "Hello, World! This is a test."
cleaned_test = clean_text(test_text)
print(f"\nТестирование функции clean_text:")
print(f"Исходный текст: {test_text}")
print(f"Очищенный текст: {cleaned_test}")
