"""ODD_EVEN"""


def main():
    """Input"""
    value1 = int(input())
    value1 = value1%2
 
    if value1 == 0:
        print("False")
    else:
        print("True")

main()
