def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

# Test the code
num = int(input("Enter a positive integer: "))
fib_sequence = fibonacci(num)
print("F({}) = {}".format(num, fib_sequence))