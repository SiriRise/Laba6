# Вариант 22
# Составьте все различные лексемы, переставляя буквы в слове «институт»
# 1 часть – написать программу в соответствии со своим вариантом задания.

word = "институт"
def find_permutations(string):
    if not string:
        yield string
    else:
        used_characters = set()
        for i, ch in enumerate(string):
            if ch not in used_characters:
                used_characters.add(ch)
                remaining_characters = string[:i] + string[i + 1:]
                for permutation in find_permutations(remaining_characters):
                    yield ch + permutation

permutations = list(find_permutations(word))
for i, permutation in enumerate(set(permutations)):
    print(f"{i + 1}: {permutation}")
