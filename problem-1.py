def sum_multiples_3_or_5(upper_limit: int):
    multiples_of_3_or_5 = []
    for number in range(1, upper_limit):
        if number % 3 == 0 or number % 5 == 0:
            multiples_of_3_or_5.append(number)

    return sum(multiples_of_3_or_5)
            



if __name__ == "__main__":
    sum_multiples_3_or_5(upper_limit=1000)