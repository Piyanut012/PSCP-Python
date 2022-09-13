"""Day I"""

def main():
    """output"""
    num = int(input())

    if num % 4 == 0 and num % 100 != 0:
        print("Yes")
    elif num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
        print("Yes")
    elif num%100 == 0 and num%400 == 0:
        print("Yes")
    else:
        print("No")

main()
