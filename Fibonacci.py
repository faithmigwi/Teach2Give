#Question 2:Write a program to generate the Fibonacci sequence up to 100.


def generate_fibonacci_sequence():
    sequence = [0, 1]
    
    while sequence[-1] + sequence[-2] <= 100:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    
    return sequence

fibonacci_sequence = generate_fibonacci_sequence()

print(fibonacci_sequence)

