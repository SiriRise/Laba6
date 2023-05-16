# Вариант 22
# Составьте все различные лексемы, переставляя буквы в слове «институт»
# 1 часть – написать программу в соответствии со своим вариантом задания.

word = "институт"
lexems = set()
def generate_lexems(word, lexems, prefix="", length=1):
    if length > 1 and prefix not in lexems:
        lexems.add(prefix)
    if length == len(word):
        if word not in lexems:
            lexems.add(word)
        return
    for i in range(len(word)):
        char = word[i]
        if i == 0 or word[i] != word[i-1]:
            generate_lexems(word[:i] + word[i + 1:], lexems, prefix + char, length + 1)


generate_lexems(word, lexems)
print(f"Лексемы в слове '{word}':")
for i, lexem in enumerate(sorted(lexems), 1):
    print(f"{i}. {lexem}")
