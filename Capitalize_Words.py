#Question 4: Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.

def capitalize_words(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result
string = input("Enter a string: ")
result = capitalize_words(string)
print(result)

