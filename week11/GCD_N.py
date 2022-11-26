"""GCD_N"""

def main(num):
    """Input"""
    var = [int(input()) for _ in range(num)]
    if num == 1:
        return print(*var)
    var.sort()
    gcd = 0
    for i in range(len(var)):
        if i != len(var) - 1:
            if gcd == 0:
                num1 = var[i]
            else:
                num1 = gcd
            num2 = var[i+1]
            while num1 != 0:
                num1, num2 = num2%num1, num1
            gcd = num2
    print(gcd)
main(int(input()))
