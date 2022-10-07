"""BTSMRT"""


def main():
    """Input"""
    daytype = input()
    age = float(input())
    height = float(input())
    if daytype == "Children Day" and age < 14 and height <= 140:
        print("FREE")
    elif daytype == "Senior Day" and age >= 60:
        print("FREE")
    elif daytype == "Normal Day" and age < 14 and height < 90:
        print("FREE")
    elif daytype == "Senior Day" and age < 14 and height < 90:
        print("FREE")
    else:
        print("PAY")

main()
