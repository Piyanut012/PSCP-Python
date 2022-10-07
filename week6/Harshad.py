"""Harshad"""


def main():
    """Input"""
    total = 0
    for _ in range(10):
        number = input()
        for i in number:
            if i == "-":
                continue
            total += int(i)
        if total == 0:
            print("No")
            continue
        if int(number) % total == 0:
            print("Yes")
        else:
            print("No")
        total = 0

main()

