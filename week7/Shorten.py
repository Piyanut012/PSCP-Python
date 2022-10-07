"""Shorten"""


def main():
    """Input"""
    first = int(input())
    before = first
    count = 1
    while first != -1:
        num = int(input())
        if num == -1:
            if count < 2:
                message = before
            print(message)
            break
        if before + 1 == num:
            message = "%d-%d" %(first, num)
            count += 1
        else:
            if count < 2:
                message = before
            print(message, end=", ")
            count = 1
            first = num
        before = num
main()
