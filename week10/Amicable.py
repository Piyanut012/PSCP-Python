"""Amicable"""

def func(number):
    """Function """
    proper = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            proper += i + number // i
    return proper

def main(range_total, amicable):
    """Input"""
    for i in range(2, range_total + 1):
        if i not in amicable:
            number = func(i)
            if func(number) == i and i != number:
                amicable.append(i)
                amicable.append(number)
    print(sum(amicable))
main(int(input()), [])
