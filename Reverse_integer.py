#question 5: Write a program that takes an integer as input and returns an integer with reversed digit
ordering.

def reverse_integer(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num
num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(reversed_num)

