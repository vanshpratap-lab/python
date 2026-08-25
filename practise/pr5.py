words = input("please enter your word : ")
vowels = ["a","e","i","o","u"]
vowel_count = 0
for chr in words:
    if chr in vowels:
        vowel_count += 1
print(vowel_count)