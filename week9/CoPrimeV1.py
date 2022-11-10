"""CoPrimeV1"""

def main():
    """Input"""
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        num2, num1 = num1, num2
    while num1 != 0:
        num1, num2 = num2%num1, num1
    if num2 == 1:
        print("YES\n1")
    else:
        print("NO\n%d" % num2)
main()
