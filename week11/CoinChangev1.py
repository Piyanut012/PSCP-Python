"""CoinChangev1"""

def main():
    """Input"""
    cost = int(input())
    coin_list = [25, 10, 5]
    total = 0
    for coin in coin_list:
        if cost >= coin:
            total += int(cost/coin)
            cost -= int(cost/coin) * coin
    print(total + cost)
main()
