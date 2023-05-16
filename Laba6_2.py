# Вариант 22
# Составьте все различные лексемы, переставляя буквы в слове «институт»
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
# ограничение - согласные не могут стоять рядом
# целевая функция - лексемы с наибольшим числом согласных на четных местах

word = "институт"
vowels = set("аеиоуыэюя")
usedscharacters = set()
def find_permutations(string, prev=None):
    if not string:
        yield string
    else:
        usedscharacters = set()
        for i, ch in enumerate(string):
            if prev is None or (prev not in vowels or ch not in vowels):
                if ch not in usedscharacters:
                    usedscharacters.add(ch)
                    remainingscharacters = string[:i] + string[i + 1:]
                    for permutation in find_permutations(remainingscharacters, ch):
                        yield ch + permutation

def count_consonants_on_odd_positions(string):
    consonants = set("бвгджзйклмнпрстфхцчшщ")
    count = sum(1 for i, ch in enumerate(string) if i % 2 == 0 and ch in consonants)
    return count

permutations = list(find_permutations(word))
max_count = max(count_consonants_on_odd_positions(string) for string in permutations)
if max_count == 0:
    print("Cогласных на нечетных местах нет")
else:
    print("Максимальное число согласных на нечетных местах:",max_count)
    i = 1
    for string in permutations:
        if count_consonants_on_odd_positions(string) == max_count:
            print(f"{i}. {string}")
            i+=1
