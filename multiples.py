def is_multiple_of_three(number):
    return number % 3 == 0


def is_multiple_of_five(number):
    return number % 5 == 0


def is_multiple_of_three_and_five(number):
    return is_multiple_of_three(number) and is_multiple_of_five(number)


def format(number):
    if is_multiple_of_three_and_five(number):
        return "ThreeFive"
    if is_multiple_of_three(number):
        return "Three"
    if is_multiple_of_five(number):
        return "Five"
    return str(number)

def run():
    for number in range(1, 101):
        print(format(number))

if __name__ == "__main__":
    run()