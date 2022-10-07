"""Blackjack"""


def main():
    """Input"""
    number = int(input())
    total = 0
    ace = 0
    if number == 2:
        first = input()
        second = input()
        save = [first, second]
    elif number == 3:
        first = input()
        second = input()
        third = input()
        save = [first, second, third]
    for i in range(0, len(save)):
        if save[i].isnumeric():
            save[i] = int(save[i])
        elif save[i] == 'J':
            save[i] = 10
        elif save[i] == 'Q':
            save[i] = 10
        elif save[i] == 'K':
            save[i] = 10
        elif save[i] == 'A':
            save[i] = 11
            ace = ace + 1
        total = total + save[i]
    if ace == 3:
        total = total - 20
    elif ace == 2 and total == 32:
        total = total - 20
    elif ace == 2 and total > 21:
        total = total - 10
    elif ace == 1 and total > 21:
        total = total - 10

    print(total)


main()
