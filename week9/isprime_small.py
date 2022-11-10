"""isprime_small"""

def main():
    """Input"""
    num = int(input())
    if num <= 0:
        num = int(str(num)[1:])
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
        if count >= 3:
            break
    if count < 2 and count != 0:
        print("Yes")
    else:
        print("No")
main()
