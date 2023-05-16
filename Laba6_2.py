# Вариант 22
# Составьте все различные лексемы, переставляя буквы в слове «институт»
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
# ограничение - согласные не могут стоять рядом
# целевая функция - лексемы с наибольшим числом согласных на четных местах

word = "институт"
lexems = set()
def generate_lexems_no_cogl(word, lexems, prefix="", length=1, prev_vowel=False, prev_char=""):
    if length == len(word):
        if word not in lexems:
            lexems.add(word)
        return

    for i, char in enumerate(word):
        is_vowel = char in "бвгджзйклмнпрстфхцчшщ"
        has_double_vowels = is_vowel and prev_vowel
        if prev_char and is_vowel and prev_char in "бвгджзйклмнпрстфхцчшщ":
            continue
        if not has_double_vowels and prefix + char not in lexems:
            lexems.add(prefix + char)
        generate_lexems_no_cogl(word[:i] + word[i + 1:], lexems, prefix + char, length + 1, is_vowel, char)


def max_consonants_on_even_indexes(lexems):
    max_count = 0
    max_lexems = []
    for lexem in lexems:
        count = sum(1 for i, char in enumerate(lexem) if i % 2 != 0 and char not in "аеёиоуыэюя" and i != 0)
        #
        if count > max_count:
            max_count = count
            max_lexems = [lexem]
        elif count == max_count:
            max_lexems.append(lexem)
    return max_lexems, max_count



generate_lexems_no_cogl(word, lexems)


max_lexems, max_count = max_consonants_on_even_indexes(lexems)
print(f"\nМаксимальное число согласных на четных местах: {max_count}")
print("Лексемы с максимальным числом согласных на четных местах:")
for i, lexem in enumerate(max_lexems, 1):
    print(f"{i}. {lexem}")
