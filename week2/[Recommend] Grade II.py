"""Grade II"""


def main():
    """Input"""
    value = float(input())
    if value < 0  or  value > 100:
        return "ERR"
    elif value >= 95:
        return "A"
    elif value >= 90:
        return "B+"
    elif value >= 85:
        return "B"
    elif value >= 80:
        return "D+"
    elif value >= 75:
        return "D"
    elif value >= 70:
        return "C+"
    elif value >= 65:
        return "C"
    elif value >= 60:
        return "F+"
    else:
        return "F"

print(main())
