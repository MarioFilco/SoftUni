word = input()
sum_vowels_letters = 0
vowels_letters_dict = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}
for l in word:
    if l in vowels_letters_dict.keys():
        sum_vowels_letters += vowels_letters_dict[l]
print(sum_vowels_letters)

# word = input()
# sum_vowels_letters = 0
#
# for letter in word:
#     if letter == 'a':
#         sum_vowels_letters += 1
#     elif letter == 'e':
#         sum_vowels_letters += 2
#     elif letter == 'i':
#         sum_vowels_letters += 3
#     elif letter == 'o':
#         sum_vowels_letters += 4
#     elif letter == 'u':
#         sum_vowels_letters += 5
# print(sum_vowels_letters)
