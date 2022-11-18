"""3nPlus1"""

def plus(num, count):
    """Function 3nPlus1"""
    if num == 1:
        return count
    if num%2 == 0:
        num = num/2
    else:
        num = num*3 + 1
    return plus(num, count + 1)

def main():
    """Input"""
    while True:
        num = int(input())
        if num == 0:
            break
        print(plus(num, 1))
main()
