'''HowLong'''

def main():
    """Input"""
    num = int(input())
    total = 0
    if num >= 0:
        for _ in str(num):
            total += 1
        print(total)
    else:
        for _ in str(num):
            total += 1
        print(total - 1)
main()
