def analyze_string(s):
    vowels = "aeiouAEIOU"
    vowel_letters = ""
    consonant_letters = ""
    count = 0

    for letter in s:
        if letter.isalpha():
            if letter in vowels:
                vowel_letters = vowel_letters + letter
                count = count + 1
            else:
                consonant_letters = consonant_letters + letter

    return (vowel_letters, count, consonant_letters)

text = input("Enter English text: ")
result = analyze_string(text)

print(f"{result[0]},{result[1]},{result[2]}")
