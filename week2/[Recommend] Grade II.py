"""Grade II"""


def main():
    """Input"""
    value = float(input())
    if value < 0  or  value > 100:
        print("ERR")
    elif value >= 95:
        print("A")
    elif value >= 90:
        print("B+")
    elif value >= 85:
        print("B")
    elif value >= 80:
        print("C+")
    elif value >= 75:
        print("C")
    elif value >= 70:
        print("D+")
    elif value >= 65:
        print("D")
    elif value >= 60:
        print("F+")
    else:
        print("F")

main()
