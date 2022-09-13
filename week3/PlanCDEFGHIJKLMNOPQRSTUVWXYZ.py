"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""

def main():
    """Input"""
    option = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if option == "Ascend":
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        if num1 > num2:
            num1, num2 = num2, num1
        if num2 > num3:
            num2, num3 = num3, num2
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))
    if option == "Descend":
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 < num3:
            num2, num3 = num3, num2
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))

main()
