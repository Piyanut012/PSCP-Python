"""Backward"""


def main():
    """Input"""
    box = []
    while True:
        message = input()
        if message == "NULL":
            break
        box.append(message)
    box.sort()
    for i in box:
        print(i)

main()
