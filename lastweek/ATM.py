"""ATM"""

def main():
    """Input"""
    money = int(input())
    while True:
        action = input()
        if action == 'END':
            print(money)
            break
        money_action = int(action[2:])
        if action[0] == "D":
            money += money_action
        elif action[0] == "W" and money-money_action >= 0:
            money -= money_action
        else:
            money = 0
main()
