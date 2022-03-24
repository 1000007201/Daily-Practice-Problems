string_ = "This is a string"

vowels = ['a', 'e', 'i', 'o', 'u']
cons = 0
vowel = 0
for i in string_:
    if i.lower() in vowels:
        vowel += 1
    if i == ' ':
        continue
    else:
        cons += 1

print(f"Vowels: {vowel}\nConsonants: {cons}")
