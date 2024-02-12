#Quetion 3 :Write a program that takes an integer as input and returns true if the input is a power of two.

def is_power_of_two(num):
    if num > 0 and (num & (num - 1)) == 0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
result = is_power_of_two(num)
print(result)
