text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count += 1

print("Number of consonants in the string:", count)