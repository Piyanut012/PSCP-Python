"""One For All"""


def main(num):
    """Input"""
    total = ""
    for i in range(1, num+1):
        name = input()
        if i == num:
            print(total + name + "_%d" % num)
        elif i % 2 == 0:
            total += name + ("-" * i)
        else:
            total += name + ("*" * i)


main(int(input()))

