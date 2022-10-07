"""Milk"""

def main():
    """Input"""
    price = int(input())
    pro = int(input())
    free = int(input())
    money = int(input())
    total_milk = 0
    total_milk += money//price
    lid = total_milk
    if pro != 0:
        while lid >= pro:
            give = (lid//pro)*free
            total_milk += give
            lid -= (lid//pro)*pro
            lid += give
    print(total_milk)
main()

