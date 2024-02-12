#Question 6:Write a program that counts the number of vowels in a sentence.
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
sentence = input("Enter a sentence: ")
num_vowels = count_vowels(sentence)
print("The number of vowels in the sentence is:", num_vowels)

