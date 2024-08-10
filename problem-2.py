def sum_even_fibonacci_numbers():
    fibonacci = [1, 2]
    while True:
        ele = fibonacci[-1] + fibonacci[-2]
        if ele < 4000000:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        else:
            break

    return sum([num for num in fibonacci if num % 2 == 0])


if __name__ == "__main__":
    print(sum_even_fibonacci_numbers())