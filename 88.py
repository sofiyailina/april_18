from itertools import permutations
letters = "МИТРОФАН"
count = 0
for code in permutations(letters, 6):
    code = ''.join(code)
    vowel_count = (code.count("И") +
                   code.count("О") + code.count("А"))
    if vowel_count < 3:
        double_vowels = [
            'ИО', "ОИ", "ИА", "АИ", "ОА", "АО"
        ]
        for v in double_vowels:
            if v in code:
                break
            else:
                count += 1
print(count)