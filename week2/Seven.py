"""Seven"""


def main():
    """Input"""
    value = int(input())
    if value > 4000000:
        value = value % 4
        if value == 1:
            print(7)
        if value == 2:
            print(9)
        if value == 3:
            print(3)
        if value == 4:
            print(1)

main()
